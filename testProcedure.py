import unittest

from tokenReader import tokenReader
from value import Value
from Eval import evaluate1
from Expression import Expression


class TestBackToCode(unittest.TestCase):
    def testBackToCode(self):
        token_reader = tokenReader("(define (f x) (+ x 2)) (f 8)")
        token = token_reader.getNext()
        self.assertEqual(token, "(define (f x) (+ x 2))")

        value = Value(Expression(token).getList())
        eval = evaluate1()
        eval.eval(value.getList())
        env = eval.getStack()[-1]
        #print(env)
        self.assertEqual('f' in env, True)
        token = token_reader.getNext()
        #self.assertEqual(token, "(define a 5)")

       
        



       
if __name__=="__main__":
    unittest.main()


