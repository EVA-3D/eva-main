import re
from typing import List
from pydantic import BaseModel, validator


PTFE_PATTERN = re.compile(r"PTFE\ (?P<length>\d+\.\d+)mm")


class ItemSource(BaseModel):
    configuration: str
    did: str
    eid: str
    wvm_type: str
    wvm_id: str
    part_id: str


class BOMItem(BaseModel):
    name: str
    description: str
    material: str
    quantity: float
    source: ItemSource

    @validator("name")
    def validate_name(value):
        match = PTFE_PATTERN.match(value)
        if match:
            return re.sub(r"\d+\.\d+", str(round(float(match.group("length")), 2)), value)
        return value

    @property
    def is_printable(self):
        return self.material.upper() in ("PETG", "ABS", "ASA", "PLA")


class BOMTable(BaseModel):
    name: str
    items: List[BOMItem]

    @classmethod
    def parse_onshape(cls, assembly_name, onshape_data):
        return cls(
            name=assembly_name,
            items=[
                BOMItem(
                    name=item["name"],
                    description=item["description"],
                    material=item["material"]["id"]
                    if isinstance(item["material"], dict)
                    else item["material"],
                    quantity=item["quantity"],
                    source=ItemSource(
                        configuration=item["itemSource"]["fullConfiguration"],
                        did=item["itemSource"]["documentId"],
                        eid=item["itemSource"]["elementId"],
                        wvm_type=item["itemSource"]["wvmType"],
                        wvm_id=item["itemSource"]["wvmId"],
                        part_id=item["itemSource"]["partId"],
                    ),
                )
                for item in onshape_data["bomTable"]["items"]
            ],
        )
