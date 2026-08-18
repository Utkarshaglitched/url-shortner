from fastapi import FastAPI, HTTPException
from model import URLReceiver
from services import ShortCodeGenerator
from fastapi.middleware.cors import CORSMiddleware
from database import add_into,read_long,read_short,read_all
from fastapi.responses import RedirectResponse, FileResponse
import os

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.get("/")
def home():
    index_path = os.path.join(BASE_DIR, "templates", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    raise HTTPException(status_code=404, detail="index.html not found")

@app.get("/analytic.html")
@app.get("/analytics")
def analytics_page():
    analytic_path = os.path.join(BASE_DIR, "templates", "analytic.html")
    if os.path.exists(analytic_path):
        return FileResponse(analytic_path)
    raise HTTPException(status_code=404, detail="analytic.html not found")

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


@app.get("/analytics/data")
def analysis():
    res=read_all()
    return res


@app.get("/{short_url}")
def redirect(short_url:str):

    short_url_st,redirect_url=read_short(f"/{short_url}",0)
    if redirect_url and (short_url_st is not None):
        return RedirectResponse(url=redirect_url)
    raise HTTPException(status_code=404, detail="Short URL not found")
    