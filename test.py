import unittest

from tokenReader import tokenReader
from value import Value

class TestTokn(unittest.TestCase):
    def testBoolean(self):
        token = tokenReader("#t")
        self.assertEqual(token.getRest(), "#t")

    def testGetToken(self):
        token = tokenReader("(+ a 1) 11 ")
        #print(token.getNext())
        self.assertEqual(token.getNext(), "(+ a 1)")
        self.assertEqual(token.getNext(), "11")
    
    def testValue(self):
        token = tokenReader("#t #f")
        value1 = Value(token.getNext());
        self.assertEqual(value1.type, "Boolean");
        self.assertEqual(value1.value, True);
        value2 = Value(token.getNext());
        self.assertEqual(value2.type,"Boolean");
        self.assertEqual(value2.value, False);

if __name__=="__main__":
    unittest.main()
