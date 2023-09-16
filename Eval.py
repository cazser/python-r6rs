from value import Value
from tokenReader import tokenReader
from value import Object

def doAdd(recvlist, env):
    list1=[]
    for it in recvlist:
        if isinstance(it, list):
            eval= evaluate1(env)
            list1.append(eval.eval(it))
        else:
            innerlist=[it]
            eval= evaluate1(env)
            list1.append(eval.eval(innerlist))
    obj = Object("")

    obj.type ="Number"
    obj.name =""
    obj.value = 0
    for item in list1:
        obj.value = obj.value+ item.value
    return obj


native_env={"+": doAdd};



class evaluate1:
    def __init__(self, env=native_env) -> None:
        self.__env__ = native_env
        

    def eval(self,objList:list[Object]):
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
                    return self.__env__[first.name](rest, self.getEnv())
                
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