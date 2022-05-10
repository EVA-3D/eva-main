from contextlib import contextmanager
from typing import Optional, List
import warnings

from sqlalchemy import exc as sa_exc
from sqlmodel import Field, SQLModel, create_engine, Relationship, Session
from sqlmodel.sql.expression import select


warnings.simplefilter("ignore", category=sa_exc.SAWarning)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# engine = create_engine(sqlite_url, echo=True)
engine = create_engine(sqlite_url)


@contextmanager
def db_session():
    with Session(engine) as session:
        yield session


class BOMTable(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    items: List["BOMItem"] = Relationship(back_populates="bom_table")


class BOMItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    bom_name: str
    description: Optional[str]
    material: str
    quantity: float
    bom_table_id: Optional[int] = Field(default=None, foreign_key="bomtable.id")
    bom_table: Optional[BOMTable] = Relationship(back_populates="items")
    source_did: str
    source_wvm_id: str
    source_wvm_type: str
    source_eid: str
    source_part_id: str
    source_configuration: str

    @property
    def is_printable(self):
        return self.material.upper() == "PETG"


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def remove_bom_table(session, bom_table_name):
    tables = session.exec(select(BOMTable).where(BOMTable.name == bom_table_name)).all()
    for table in tables:
        items = session.exec(
            select(BOMItem).where(BOMItem.bom_table_id == table.id)
        ).all()
        for item in items:
            session.delete(item)
        session.delete(table)

    session.commit()


def get_bom_table(session, bom_table_name):
    stmt = (
        select(BOMTable)
        .where(BOMTable.name == bom_table_name)
    )
    first = session.exec(stmt).first()
    if first:
        first.items  # need to access it here for lazy load
        return first
