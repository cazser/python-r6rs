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

env = {"Add": doAdd}
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
    
    def evalist(self, list):
        token = tokenReader(list);
        #print(token.getRest())
        first =  Value(token.getNext());
        rest = []
        while not token.isEnd():
            rest.append(self.eval( Value(token.getNext())))
        return self.env[first.name](rest)

if __name__=='__main__':
    token2 = tokenReader("(+ 1 2)")
    value4 = Value(token2.getNext());
    #print(value4.type)
    eval1= evaluate();
    print(eval1.eval(value4))