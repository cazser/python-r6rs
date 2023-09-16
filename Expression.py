from tokenReader import tokenReader;


class Expression:

    def __init__(self, token):
        self.token = token
        self.list=[]
        if token[0]=='(':
            self.type ="Compose"
            self.code = token[1:-1]
            tokens = tokenReader(self.code);
            while not tokens.isEnd():
                t = Expression(tokens.getNext());
                if t.getType() =="Single":
                    self.list.append(t.getCode())
                else:
                    self.list.append(t.getList());
            
        else:
            self.type ="Single"
            self.code = token
            self.list.append(token);

    def getList(self):
        return self.list

    def getType(self):
        return self.type

    def getInside(self):
        return self.code
    
    def getCode(self):
        return self.token


    def __str__(self) -> str:
        return str(self.list)