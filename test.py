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

class TestValue(unittest.TestCase):    
    def testValue(self):
        token = tokenReader("#t #f")
        value1 = Value(token.getNext());
        self.assertEqual(value1.type, "Boolean");
        self.assertEqual(value1.value, True);
        value2 = Value(token.getNext());
        self.assertEqual(value2.type,"Boolean");
        self.assertEqual(value2.value, False);
        self.assertEqual(token.isEnd(), True);
        token1 = tokenReader("123");
        value3 = Value(token1.getNext());
        self.assertEqual(value3.type,"Number");
        self.assertEqual(value3.value, 123);
        token2 = tokenReader("(+ 1 2)")
        value4 = Value(token2.getNext());
        self.assertEqual(value4.type, "Expression")
        self.assertEqual(value4.inside, "+ 1 2")

 
class TestEval(unittest.TestCase):
    def testEval(self):
        token = tokenReader("(+ 1 2 3)")
        value = Value(token.getNext())
        eval = evaluate1();
        self.assertEqual(eval.eval(value).value, 6)
        token1 = tokenReader("(- 6 1 3)")
        value1 = Value(token1.getNext())
        eval1 = evaluate1();
        self.assertEqual(eval1.eval(value1).value, 2)
        token2 = tokenReader("(* 6 2 3)")
        value2 = Value(token2.getNext())
        eval2 = evaluate1();
        self.assertEqual(eval2.eval(value2).value, 36)
        token3 = tokenReader("(/ 24 2 3)")
        t = token3.getNext();
        #print(t);
        value3 = Value( t );
        self.assertEqual(eval1.eval(value3).value, 4);
        token4 = tokenReader("(* (+ 1 2) (/ 24 2 3))")
        t = token4.getNext();
        #complex aritemetic
        value4 = Value( t );
        self.assertEqual(eval1.eval(value4).value, 12);
        







if __name__=="__main__":

    unittest.main()
