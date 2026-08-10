from fastapi import FastAPI
from model import URLReceiver
from services import ShortCodeGenerator
from model import URL

app=FastAPI()


app.post("/api/urls")
def new_url(data:URLReceiver):

    short_url=ShortCodeGenerator.generator()

    url_pairs=(data.long_url,short_url)
    
    
