import secrets
import string


class ShortCodeGenerator:

    characters=string.ascii_letters+string.digits
    
    def __init__(self,length=6):
        self.length=length

    def generator(self):
        code=[secrets.choice(self.characters) for x in range (self.length)]

        return f"/{"".join(code)}"


