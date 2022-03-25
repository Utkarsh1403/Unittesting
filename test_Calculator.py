import Calculator
import unittest

class TestClass(unittest.TestCase):

    def test_Add(self):
        x = 10
        y = 20
        result = Calculator.add(x,y)
        self.assertEqual(result,x+y)

    def test_sub(self):
        x = 20
        y = 10
        result = Calculator.sub(x,y)
        self.assertEqual(result,x-y)







if __name__ =="__main__":
    unittest.main()