from value import Value
from tokenReader import tokenReader

native_env={};

class evaluate1:
    def __init__(self, env=native_env) -> None:
        self.__env__ = native_env
        

    def eval(self,value:Value):
        objList = value.getList();
        if len(objList)>1:
            first = objList[0];
            rest = objList[1:];
            if first.type=='keyword':
                if first.name=='define':
                    self.__env__[rest[0].name] = rest[1]
                    return None
        elif len(objList)==1:
            first = objList[0]
            if first.type=="Identifier":
                return self.__env__[first.name]
    
    def getEnv(self):
        return self.__env__;

if __name__=='__main__':
    pass