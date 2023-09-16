


import string


class Object:
    
    def __init__(self, str:string) -> None:
        self.name=""
        self.type=None 
        self.value=None
        keywords=["define"]
        if len(str)>0:
            if str in keywords:
                self.type="keyword"
                self.name = str
            elif str=='+':
                self.type="op"
                self.name=str
            elif str=='-':
                self.type="op"
                self.name=str
            elif str=='*':
                self.type="op"
                self.name=str
            elif str=='/':
                self.type="op"
                self.name=str
            elif  str[0]=='-' and str[1] in '0123456789':
                self.type = "Number"
                self.value = int(str)
            elif str[0] in "0123456789":
                self.type = "Number"
                self.value = int(str)
            else:
                self.type="Identifier"
                self.value=None
                self.name = str 

    def __str__(self) -> str:
        return str({"type": self.type, "value": self.value, "name": self.name})        
        

class Value:

    def __init__(self, tokenlist):
        self.list=[]
        for it in tokenlist:
            if isinstance(it, list):
                inner = Value(it)
                self.list.append(inner.getList())
            else:
                self.list.append(Object(it))

        

    def getList(self):
        return self.list
    
    


    def __str__(self) -> str:
        pass