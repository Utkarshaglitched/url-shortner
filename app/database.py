import os
from dotenv import load_dotenv
from sqlalchemy import create_engine,select
from sqlalchemy.orm import Session
from model import Base,URLModel
import json

load_dotenv()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url)

Base.metadata.create_all(engine)


def get_session():
    return Session(engine)

def add_into(short_url,long_url):
    session=get_session()
    try:
        db_data=URLModel(short_code=short_url,
                         original_url=long_url,
                         clicks=0)
        
        session.add(db_data)
        session.commit()
        
        return True,""

    except Exception as e:
        session.rollback()
        return False,str(e)

    finally:
        session.close()

def read_short(short_url,task):
    session=get_session()
    try:
        command=select(URLModel).where(URLModel.short_code==short_url)

        result=session.execute(command)

        fnd=result.scalar_one_or_none()

        if fnd is not None:
            if task==0:
                if fnd.clicks is None:
                    fnd.clicks = 0
                fnd.clicks += 1
                session.commit()

            return fnd,fnd.original_url
        else:
            return None,""

    except Exception as e:
        session.rollback()
        return None, ""

    finally:
        session.close()

def read_long(long_url):
    session=get_session()
    try:
        command=select(URLModel).where(URLModel.original_url==long_url)

        result=session.execute(command)

        fnd=result.scalar_one_or_none()

        return fnd

    except:
        return None

    finally:
        session.close()

def read_all():
    session=get_session()
    try:
        command=select(URLModel)
        result=session.execute(command)
        result=result.scalars().all()

        response_list=[]
        for urls in result:
            response_list.append(
            {
                "short_url":urls.short_code,
                "original_url":urls.original_url,
                "clicks":urls.clicks if urls.clicks is not None else 0
            }
            )

        return response_list
        
    except:
        return []
    finally:
        session.close()