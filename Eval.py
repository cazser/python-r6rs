import string
from value import Value
from tokenReader import tokenReader
from value import Object





class evaluate1:
    def __init__(self, stack=[{}]) -> None:
        self.__stack__ = stack
        self.op={
            "+":self.doAdd,
        }

    def doAdd(self, recvList):
        eval1 = evaluate1(self.__stack__)
        #for it in recvList:
        #    print(it)
        list1=[]
        for it in recvList:
            if isinstance(it, list):
                list1.append(eval1.eval(it))
            else:
                list1.append(eval1.eval([it]))

        obj = Object("0")
        for it in list1:
            obj.value = obj.value + it.value
        return obj

    def eval(self, objList: list[Object]):
        """
        for it in objList:
            print(it)
        """
            
        if len(objList)>1:
            first = objList[0]
            rest = objList[1:]
            #print(first["type"]=="keyword")
            if first["type"] =="keyword":
                if first["name"] == "define":
                    self.defineVar(rest[0], rest[1])
            elif first["type"] =="op":
                return self.op[first.name](rest)
        else:
            if objList[0]["type"] in ["Number"]:
                return objList[0]
            else:
                name = objList[0]["name"]
                return self.lookUp(name)
            
    def defineVar(self, item1, item2):
        if isinstance(item1, list):
            pass
        else:
            self.__stack__[-1][item1['name']] = item2

    def getStack(self):
        return self.__stack__

    def lookUp(self, name:string):
        for index in range(len(self.__stack__)):
            if name in self.__stack__[-1 - index]:
                return self.__stack__[-1-index][name]
        return None            

if __name__=='__main__':
    pass