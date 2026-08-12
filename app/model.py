from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column

class URLReceiver(BaseModel):
    long_url:str



class Base(DeclarativeBase):
    pass


class URLModel(Base):

    __tablename__="urls"

    id:Mapped[int]=mapped_column(primary_key=True)
    short_code:Mapped[str]=mapped_column(unique=True,index=True)
    original_url:Mapped[str]=mapped_column()
    clicks:Mapped[int]=mapped_column(default=0)  