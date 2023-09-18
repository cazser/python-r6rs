from value import Value
from tokenReader import tokenReader
from value import Object





class evaluate1:
    def __init__(self, stack=[]) -> None:
        self.__stack__ = stack
    
    def eval(self, objList: list[Object]):
        for it in objList:
            print(it)
        if len(objList)>1:
            first = objList[0]
            rest = objList[1:]
            if first["type"] =="keyword":
                if first["name"] == "define":
                    self.defineVar(rest[0], rest[1])
            
    def defineVar(self, item1, item2):
        pass

    def getStack(self):
        return self.__stack__    

if __name__=='__main__':
    pass