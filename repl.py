from tokenReader import tokenReader
from value import Value
from Eval import evaluate1
from Expression import Expression
def repl():
    prompt="<"
    prompt1=">"
    index = 1
    line=""
    while not line=="#quit":
        print(prompt+ str(index) + prompt1, end="")
        line=input();
        token_Reader = tokenReader(line)
        eval = evaluate1()
        while not token_Reader.isEnd():
            t= token_Reader.getNext()
            #print(t)
            exp = Expression(t)            
            value = Value(exp.getList())
            
            result= eval.eval(value.getList())
            env = eval.getStack()
            #for key, v in env.items():
            #    print(key, v)

            if not result== None:
                if isinstance(result, dict):
                    print(result["value"])
                else:
                    print(result.value)
            index= index+1
    print("thanks")

 