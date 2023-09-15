from value import Value
from tokenReader import tokenReader
def doAdd(list):
    #print("here")
    value = Value("")
    value.type = "Number"
    cc = 0;
    for it in list:
        #print(it)
        cc = cc+ it.value;
    value.value = cc
    return value

def doSub(list):
    #print("here")
    value = Value("")
    value.type = "Number"
    cc = list[0].value;
    for i in range(1, len(list)):
        #print(it)
        it = list[i];
        cc = cc- it.value;
    value.value = cc
    return value

def doMult(list):
    #print("here")
    value = Value("")
    value.type = "Number"
    cc = 1;
    for it in list:
        #print(it)
        cc = cc* it.value;
    value.value = cc
    return value
    


def doDiv(list):
    #print("here")
    value = Value("")
    value.type = "Number"
    cc = list[0].value;
    for i in range(1, len(list)):
        #print(it)
        it = list[i];
        cc = cc// it.value;
    value.value = cc
    return value


def doDefine(list):
    env[list[0]] = list[1]
    print(list[0])
    print(list[1])

env = {"Add": doAdd, "Sub": doSub, "Mult": doMult, "Div": doDiv, "define": doDefine}
class evaluate1:
    def __init__(self, env=env) -> None:
        self.env=env
    def eval(self,value):
        if value.type=="Boolean":
            return value
        elif value.type=='Number':
            return value
        elif value.type=='Expression':
            #print("Mark")
            return self.evalist(value.inside)
        elif value.type=="Idenetifier":
            print(self.env)
            return env[value.name]
        
    def evalist(self, list):
        token = tokenReader(list);
        #print(token.getRest())
        first =  Value(token.getNext());
        print(first)     
           
        rest = []
        while not token.isEnd():
            rest.append(self.eval( Value(token.getNext())))
        for it in rest:
            print(it);
        return self.env[first.name](rest)

if __name__=='__main__':
    token2 = tokenReader("(+ 1 2)")
    value4 = Value(token2.getNext());
    #print(value4.type)
    eval1= evaluate1();
    print(eval1.eval(value4))