import unittest

from tokenReader import tokenReader
from value import Value
from Eval import evaluate1
from Expression import Expression

class TestBasicValue(unittest.TestCase):
    def testNumber(self):
        token_reader = tokenReader("(define a 5) a")
        value = Value(Expression(token_reader.getNext()).getList())
        eval = evaluate1()
        eval.eval(value.getList())
        #stack = eval.getStack()
        value = Value(Expression(token_reader.getNext()).getList())
        result =eval.eval(value.getList())
        print(result)
        

if __name__=="__main__":
    unittest.main()
