import asyncio
import re
from base64 import b64encode
from datetime import datetime
from urllib.parse import urlencode, urlparse, parse_qsl
from secrets import token_urlsafe

import aiohttp
import hashlib
import hmac


ONSHAPE_URL_PATTERN = re.compile(r"(https://cad.onshape.com/documents)?/?(?P<did>.*)/w/(?P<wid>.*)/e/(?P<eid>.*)")


class Onshape:
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key

        self.session = aiohttp.ClientSession()

    def __generate_hmac(self, hmac_str):
        return hmac.new(
            self.secret_key.encode(), hmac_str, digestmod=hashlib.sha256
        ).digest()

    def sign_request(self, method, path, query, headers):
        if not query:
            query = ""
        query = urlencode(query)
        nonce = token_urlsafe(25)
        method = method.lower()
        date = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

        hmac = b64encode(
            self.__generate_hmac(
                f"{method}\n{nonce}\n{date}\n{headers['Content-Type']}\n{path}\n{query}\n".lower().encode()
            )
        )

        headers["Date"] = date
        headers["On-Nonce"] = nonce
        headers["Authorization"] = f"On {self.access_key}:HmacSHA256:{hmac.decode()}"

    async def __call(
        self,
        method,
        path,
        headers=None,
        query=None,
        json=None,
        base_url="https://cad.onshape.com",
    ):
        if not headers:
            headers = {}
        headers["Content-Type"] = "application/json"
        self.sign_request(method, path, query, headers)

        async with getattr(self.session, method.lower())(
            url=base_url + path,
            json=json,
            headers=headers,
            params=query,
            allow_redirects=False,
        ) as resp:
            if resp.status == 200 and resp.content_type == "application/json":
                response_data = await resp.json()
                return response_data
            elif resp.status == 307:
                url = urlparse(resp.headers["Location"])
                query = dict(parse_qsl(url.query))
                return await self.__call(
                    "get",
                    url.path,
                    query=query,
                    base_url=f"{url.scheme}://{url.netloc}",
                )
            elif resp.status >= 400:
                raise Exception(await resp.read())
            else:
                return await resp.read()

    @staticmethod
    def link(did_wid_eid_url: str):
        match = ONSHAPE_URL_PATTERN.match(did_wid_eid_url)
        if not match:
            raise ValueError("Not an onshape URL or element string")
        return {
            "did": match.group("did"),
            "wid": match.group("wid"),
            "eid": match.group("eid"),
        }

    async def get_element_configuration(self, did, wid, eid):
        return await self.__call(
            "get",
            f"/api/elements/d/{did}/w/{wid}/e/{eid}/configuration",
            query={},
        )

    async def get_assembly(self, did, wid, eid):
        return await self.__call(
            "get",
            f"/api/assemblies/d/{did}/w/{wid}/e/{eid}",
            query={},
        )

    async def get_assembly_bom(self, did, wid, eid):
        return await self.__call(
            "get",
            f"/api/assemblies/d/{did}/w/{wid}/e/{eid}/bom",
            query={
                "generateIfAbsent": "true",
                "multiLevel": "true",
                "indented": "false",
            },
        )

    async def get_translation_formats(self, did):
        return await self.__call(
            "get",
            f"/api/translations/d/{did}",
        )

    async def export_part(self, did, wvm_id, wvm_type, eid, part_id, configuration):
        return await self.__call(
            "get",
            f"/api/partstudios/d/{did}/{wvm_type}/{wvm_id}/e/{eid}/stl",
            query={
                "mode": "binary",
                "partIds": part_id,
                "grouping": "false",
                "units": "millimeter",
                "configuration": configuration,
            },
        )

    async def translate_partstudio_to_step(self, did, wvm_id, wvm_type, eid, part_id, configuration):
        return await self.__call(
            "post",
            f"/api/partstudios/d/{did}/{wvm_type}/{wvm_id}/e/{eid}/translations",
            json={
                "elementId": eid,
                "emailLink": False,
                "flattenAssemblies": False,
                "grouping": True,
                "includeExportIds": False,
                "partIds": part_id,
                "configuration": configuration,
                "formatName": "STEP",
                "stepVersionString": "AP242",
                "storeInDocument": False,
                "triggerAutoDownload": False,
                "yAxisIsUp": False,
            },
        )

    async def get_translation_status(self, tid):
        return await self.__call(
            "get",
            f"/api/translations/{tid}",
        )

    async def get_document_external_data(self, did, fid):
        return await self.__call(
            "get",
            f"/api/documents/d/{did}/externaldata/{fid}",
        )

    async def export_to_step(self, did, wvm_id, wvm_type, eid, part_id, configuration):
        # initialte translation to STEP
        translation = await self.translate_partstudio_to_step(did=did,wvm_id=wvm_id, wvm_type=wvm_type, eid=eid, part_id=part_id, configuration=configuration)
        while True:
            # wait for the traslation to finish
            status = await self.get_translation_status(tid=translation["id"])
            if status["requestState"].upper() == "DONE":
                # translation is done
                break
            await asyncio.sleep(2)

        for fid in status["resultExternalDataIds"]:
            # NOT Supporting multiple downloads for now
            return await self.get_document_external_data(did=did, fid=fid)

    async def get_shaded_view(self, did, wid, eid, configuration="", height=1200, width=850):
        return await self.__call(
            "get",
            f"/api/assemblies/d/{did}/w/{wid}/e/{eid}/shadedviews",
            query={
                "configuration": configuration,
                "viewMatrix": "trimetric",
                "outputHeight": height,
                "outputWidth": width,
                "showAllParts": "true",
                "useAntiAliasing": "true",
                "pixelSize": 0,
            },
        )

    async def close(self):
        await self.session.close()

    async def __aenter__(self) -> "Onshape":
        return self

    async def __aexit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ) -> None:
        await self.close()


