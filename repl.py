from tokenReader import tokenReader
from value import Value
from Eval import evaluate1
def repl():
    prompt="->>"
    print(prompt)
    line= input();
    while not line=="#quit":
        line=input();
        eval = evaluate1()
        print(eval.eval(Value(tokenReader(line))))
    print("thanks")

 