from fastapi import FastAPI
from model import URLReceiver
from services import ShortCodeGenerator

from database import add_into,read_long,read_short
from fastapi.responses import RedirectResponse
import json


app=FastAPI()


@app.post("/api/urls")
def new_url(data:URLReceiver):
    generator=ShortCodeGenerator()
    short_url=generator.generator()
    long_url=data.long_url

    check_long=read_long(long_url)
    if check_long is not None:
        return {"code":400,
                "msg":"already exits in database"}

    add_cmd,add_msg=add_into(short_url,long_url)
    if not add_cmd:
        return {
            "code":400,
            "msg":add_msg
        }

    return {
        "code":200,
        "msg":short_url
    }


@app.get("/{short_url}")
def redirect(short_url:str):

    short_url_st,redirect_url=read_short(f"/{short_url}",0)
    if redirect_url and (short_url_st is not None):
        return RedirectResponse(url=redirect_url)

