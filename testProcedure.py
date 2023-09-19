import unittest

from tokenReader import tokenReader
from value import Value
from Eval import evaluate1
from Expression import Expression


class TestProcedureDefine(unittest.TestCase):
    def testProcedureDefine(self):
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

    def testProcedureCall(self):
        token_reader = tokenReader("(define (f x) (+ x 2)) (define a 5) a f (f 8)")
        token = token_reader.getNext()
        self.assertEqual(token, "(define (f x) (+ x 2))")

        value = Value(Expression(token).getList())
        eval = evaluate1()
        eval.eval(value.getList())
        env = eval.getStack()[-1]
        #print(env)
        self.assertEqual('f' in env, True)
        token = token_reader.getNext()
        
        value = Value(Expression(token).getList())
        
        objList = value.getList()
        eval.eval(objList)
        env = eval.getStack()
        
        token = token_reader.getNext()
        
        value = Value(Expression(token).getList())
        
        objList = value.getList()
        eval.eval(objList)

        token = token_reader.getNext()
        
        value = Value(Expression(token).getList())
        
        objList = value.getList()
        eval.eval(objList)

        token = token_reader.getNext()
        
        value = Value(Expression(token).getList())
        
        objList = value.getList()
        eval.eval(objList)





       
if __name__=="__main__":
    unittest.main()


