import unittest
from tokenReader import tokenReader
from value import Value
from Eval import evaluate1
class TestIdentifier(unittest.TestCase):
    def testIdentifier(self):
        token = tokenReader("(define a 5) a")
        value = Value(token.getNext());
        eval = evaluate1()
        print(eval.eval(value))








if __name__=="__main__":

    unittest.main()

