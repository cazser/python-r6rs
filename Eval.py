from value import Value
from tokenReader import tokenReader

def doAdd(list):
    for it in list:
        print(it)

native_env={"+": doAdd};



class evaluate1:
    def __init__(self, env=native_env) -> None:
        self.__env__ = native_env
        

    def eval(self,objList):
        #objList = value.getList();
        if len(objList)>1:
            first = objList[0];
            rest = objList[1:];
            if first.type=='keyword':
                if first.name=='define':
                    self.__env__[rest[0].name] = rest[1]
                    return None
            elif first.type=='op':
                if first.name=='+':
                    return self.__env__[first.name](rest)
                
        elif len(objList)==1:
            first = objList[0]
            if first.type=="Identifier":
                return self.__env__[first.name]
            if first.type=="Number":
                return first
            
    def getEnv(self):
        return self.__env__;

if __name__=='__main__':
    pass