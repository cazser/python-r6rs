import unittest

from tokenReader import tokenReader
from value import Value
from Eval import evaluate1
from Expression import Expression
class TestToken(unittest.TestCase):
    def testBoolean(self):
        token = tokenReader("#t")
        self.assertEqual(token.getRest(), "#t")

    def testGetToken(self):
        token = tokenReader("(+ a 1) 11 ")
        #print(token.getNext())
        self.assertEqual(token.getNext(), "(+ a 1)")
        self.assertEqual(token.getNext(), "11")

class TestExpression(unittest.TestCase):
    def testExpression(self):
        token = tokenReader("(+ a 1) 11 ")
        #print(token.getNext())
        exp1 = Expression(token.getNext())
        self.assertEqual(exp1.getCode(), "(+ a 1)")
        self.assertEqual(exp1.getType(), "Compose")
        self.assertEqual(exp1.getInside(), "+ a 1")
        self.assertEqual(str(exp1), "['+', 'a', '1']")
        exp1 = Expression(token.getNext())
        self.assertEqual(exp1.getCode(), "11")
        self.assertEqual(exp1.getType(), "Single")
        token1 = tokenReader("(+ 2 3 (+ 3 4 (- 9 7) (+ 100 100) ) )")
        exp2 = Expression(token1.getNext());
        self.assertEqual("", str(exp2))
       





if __name__=="__main__":

    unittest.main()
