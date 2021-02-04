import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(10,10),20)
        self.assertEqual(calculator.add(10,20),30)
    def test_sub(self):
        self.assertEqual(calculator.sub(10,10),0)
        self.assertEqual(calculator.sub(20,10),0)    
    def test_mul(self):
        self.assertEqual(calculator.mul(10,10),100)
        self.assertEqual(calculator.mul(10,1),10)
    def test_div(self):
        self.assertEqual(calculator.div(10,10),1)
        self.assertEqual(calculator.div(20,10),2)

if __name__ == '__main__':
    unittest.main()
