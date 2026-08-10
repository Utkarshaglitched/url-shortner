from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column


class URL:
    def __init__(self,pair):

        self.original_url=pair[0]
        self.short_url=pair[1]


class URLReceiver(BaseModel):
    long_url:str


class Base(DeclarativeBase):
    pass


class URLModel(Base):

    __tablename__="urls"

    id:Mapped[int]=mapped_column(primary_key=True)
    short_code:Mapped[str]=mapped_column(unique=True,index=True)
    original_url:Mapped[str]=mapped_column()    