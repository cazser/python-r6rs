from value import Value
from tokenReader import tokenReader
env = {"Add": ""}
class evaluate:
    def eval(self,value):
        if value.type=="Boolean":
            return value
        elif value.type=='Number':
            return value
        elif value.type=='Expression':
            #print("Mark")
            self.evalist(value.inside)
    
    def evalist(self, list):
        token = tokenReader(list);
        #print(token.getRest())
        first =  Value(token.getNext());
        rest = []
        while not token.isEnd():
            rest.append(self.eval( Value(token.getNext())))
        for it in rest:
            print(it)

if __name__=='__main__':
    token2 = tokenReader("(+ 1 2)")
    value4 = Value(token2.getNext());
    #print(value4.type)
    eval1= evaluate();
    eval1.eval(value4)