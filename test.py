import unittest

from tokenReader import tokenReader
from value import Value
from Eval import evaluate1
class TestToken(unittest.TestCase):
    def testBoolean(self):
        token = tokenReader("#t")
        self.assertEqual(token.getRest(), "#t")

    def testGetToken(self):
        token = tokenReader("(+ a 1) 11 ")
        #print(token.getNext())
        self.assertEqual(token.getNext(), "(+ a 1)")
        self.assertEqual(token.getNext(), "11")





if __name__=="__main__":

    unittest.main()
