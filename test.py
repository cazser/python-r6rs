import unittest

from tokenReader import tokenReader
from value import Value
from Eval import evaluate1
from Expression import Expression

class TestBasicValue(unittest.TestCase):
    def testNumber(self):
        token_reader = tokenReader("(define a 5)")
        value = Value(Expression(token_reader.getNext()).getList())
        eval = evaluate1()
        eval.eval(value.getList())
        stack = eval.getStack()
        for it in stack:
            print(it)

if __name__=="__main__":
    unittest.main()
