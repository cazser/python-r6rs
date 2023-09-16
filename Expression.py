


class Expression:

    def __init__(self, token):
        self.token = token
    
    def getCode(self):
        return self.token


    def __str__(self) -> str:
        pass