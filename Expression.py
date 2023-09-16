


class Expression:

    def __init__(self, token):
        self.token = token
        self.list=[]
        if token[0]=='(':
            self.type ="Compose"
            self.code = token[1:-1]
        else:
            self.type ="Single"
            self.code = token

    def getType(self):
        return self.type

    def getInside(self):
        return self.code
    
    def getCode(self):
        return self.token


    def __str__(self) -> str:
        pass