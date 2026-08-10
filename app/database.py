import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column
load_dotenv()
databaseURL=os.getenv("DATABASE_URL")

engine=create_engine(databaseURL)

class Base(DeclarativeBase):
    pass


class URLMODEL(Base):

    __tablename__="urls"

    id:Mapped[int]=mapped_column(primary_key=True)
    short_code:Mapped[str]=mapped_column(unique=True,index=True)
    original_url:Mapped[str]=mapped_column()

Base.metadata.create_all(engine)