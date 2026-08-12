import secrets
import string
from database import read_short

class ShortCodeGenerator:

    characters=string.ascii_letters+string.digits
    
    def __init__(self,length=6):
        self.length=length

    def generator(self):
        while True:
            code=[secrets.choice(self.characters) for x in range (self.length)]

            check_sh,_=read_short(f"/{"".join(code)}",1)
            if check_sh is None:
                return f"/{"".join(code)}"

