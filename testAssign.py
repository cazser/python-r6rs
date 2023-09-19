import unittest

from tokenReader import tokenReader
from value import Value
from Eval import evaluate1
from Expression import Expression


class TestBackToCode(unittest.TestCase):
    def testBackToCode(self):
        token_reader = tokenReader("(define a 5) (set! a 12) a")
        token = token_reader.getNext()
        self.assertEqual(token, "(define a 5)")

        value = Value(Expression(token).getList())
        eval = evaluate1()
        eval.eval(value.getList())
        env = eval.getStack()
        #print(env)
        token = token_reader.getNext()
        #self.assertEqual(token, "(define a 5)")

        value = Value(Expression(token).getList())
        #eval = evaluate1()
        result =eval.eval(value.getList())
        #print(result)
        token = token_reader.getNext()
        #self.assertEqual(token, "(define a 5)")

        value = Value(Expression(token).getList())
        #eval = evaluate1()
        result =eval.eval(value.getList())
        self.assertEqual(str( result), "{'type': 'Number', 'value': 12, 'name': '', 'str': '12'}")
        
        



       
if __name__=="__main__":
    unittest.main()

