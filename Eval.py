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


def doSub(recvlist, env):
    list1=[]
    for it in recvlist:
        if isinstance(it, list):
            eval= evaluate1(env)
            list1.append(eval.eval(it))
            for item in list1:
                print(item)
        else:
            innerlist=[it]
            eval= evaluate1(env)
            list1.append(eval.eval(innerlist))
    obj = list1[0]

    
    for index in range(1, len(list1)):
        item = list1[index]
        obj.value = obj.value - item.value
    return obj



def doDefine(objList, env):
    item1 = objList[0]
    item2 = objList[1]
    if isinstance(item1, list):
        procdure= item1[0]
        arguments = item1[1:]
        body = item2 
        env[procdure.name] = {"arguments": arguments, "body": body, "type": "procedure"}
        
    else:
        env[item1.name] = item2

native_env={"+": doAdd, "-": doSub, "define": doDefine};



class evaluate1:
    def __init__(self, env=native_env, stack=[]) -> None:
        self.__env__ = native_env
        self.stack = stack
        

    def eval(self,objList:list[Object]):
        #objList = value.getList();
        if len(objList)>1:
            first = objList[0];
            rest = objList[1:];
            if first.type=='keyword':
                if first.name=='define':
                    self.__env__["define"](rest, self.getEnv())
                    return None
            elif first.type=='op':
                if first.name=='+':
                    return self.__env__[first.name](rest, self.getEnv())
                elif first.name=='-':
                    
                    return self.__env__[first.name](rest, self.getEnv())
                
            elif "type" in self.__env__[first.name] and self.__env__[first.name]["type"]=='procedure':
                #函数调用
                env = self.getEnv()
                stack=self.getStack()
                last={}
                arguments = env[first.name]["arguments"]
                for index in range(len(arguments)):
                    last[arguments[index].name] = rest[index]
                #print(last[arguments[0].name])
                stack.append(last)
                inner_evaluate = evaluate1(env, stack)
                result= inner_evaluate.eval(env[first.name]["body"])
                inner_evaluate.getStack().pop()
                return result
                
        elif len(objList)==1:
            first = objList[0]
            if first.type=="Identifier":
                if len(self.stack)>0:
                    last = self.stack[-1]
                    if first.name in last:
                        return last[first.name]
                elif  first.name in self.__env__:
                    return self.__env__[first.name]
                else:
                    return None
            if first.type=="Number":
                return first
            
    def getEnv(self):
        return self.__env__;
    
    def getStack(self):
        return self.stack
    

if __name__=='__main__':
    pass