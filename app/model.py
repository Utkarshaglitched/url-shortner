from pydantic import BaseModel
    



class URL:
    def __init__(self,pair):

        self.original_url=pair[0]
        self.short_url=pair[1]


class URLReceiver(BaseModel):
    long_url:str

