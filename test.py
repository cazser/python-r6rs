import unittest

from tokenReader import tokenReader
from value import Value
from Eval import evaluate1
from Expression import Expression


class TestBackToCode(unittest.TestCase):
    def testBackToCode(self):
        token_reader = tokenReader("(+ 1 (* 2 3 4) (* 9 0))")
        value = Value(Expression(token_reader.getNext()).getList())
        eval = evaluate1()
        objList= value.getList()
        self.assertEqual( eval.backToCode(objList), "( + 1 ( * 2 3 4 ) ( * 9 0 ) )" )
    

class TestLetStruct(unittest.TestCase):
    def testLetStruct(self):
        token_reader = tokenReader("(let ((x 5) (y 7)) (+ x y))")
        token = token_reader.getNext()
        exp = Expression(token)
        value = Value(exp.getList())
        eval = evaluate1()
        self.assertEqual(str( eval.eval(value.getList())), "{'type': 'Number', 'value': 12, 'name': '', 'str': '0'}")
        """
        for it in value.getList():
            if isinstance(it, list):
                for item in it:
                    if isinstance(item, list):
                        for cc in item:
                            print("---...", cc)
                    else:
                        print("---" , item)
            else:
                print(it)
        """
    
    def testAdd(self):
        token_reader = tokenReader("(define a 18) (define b 16) (+ a b)")
        token = token_reader.getNext()
        exp = Expression(token)
        value = Value(exp.getList())
        eval = evaluate1()
        eval.eval(value.getList())

        token = token_reader.getNext()
        exp = Expression(token)
        value = Value(exp.getList())
        
        eval.eval(value.getList())

        token = token_reader.getNext()
        exp = Expression(token)
        value = Value(exp.getList())
        
        print(eval.eval(value.getList()))


        
        



       
if __name__=="__main__":
    unittest.main()
