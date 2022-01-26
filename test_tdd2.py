import tdd2
import unittest
import math 


def func1(x): return pow(x,3) 
def func2(x): return (pow(x,0.5)) 
def func3(x): return math.log(x) 
def func4(x): return math.sin(x) 
def gap_int(func, g, p): return round(func(p),g)

class Test(unittest.TestCase): 
    def test_miroir(self):
        self.assertEqual(tdd2.miroir('abcdefg',3),'abcddcba')
        self.assertEqual(tdd2.miroir('miroir',2),'mirrim')
        self.assertEqual(tdd2.miroir('12345',4),'1234554321')
        self.assertEqual(tdd2.miroir('pog',0),'pp')
        self.assertEqual(tdd2.miroir('pog',-1),-1)

    def test_derivee(self):
        self.assertEqual(tdd2.derivee([-2.979,-1.056,0.76,2.298,4.987],2),[0.96,0.91,0.77,1.34])
        self.assertEqual(tdd2.derivee([5.029,2.498,1.409,1.409,2.409,5.209],0.5),[-5.06,-2.18,0.0,2.0,5.6])
        self.assertEqual(tdd2.derivee([2.575,2.575,2.575,2.575],1),[0,0,0])
        self.assertEqual(tdd2.derivee([1],2),False)

    def test_derivee2(self):
        self.assertEqual(tdd2.derivee2([-2.979,-1.056,0.76,2.298,4.987],2),[-0.02,-0.07,0.29])
        self.assertEqual(tdd2.derivee2([5.029,2.498,1.409,1.409,2.409,5.209],0.5),[5.76,4.36,4.0,7.2])
        self.assertEqual(tdd2.derivee2([2.575,2.575,2.575,2.575],1),[0,0])
        self.assertEqual(tdd2.derivee2([1,2],2),False)

    def test_derivee_func(self): 
        self.assertEqual(tdd2.derivee_func(func1, 0.01, -1.78), -5.64) 
        self.assertEqual(tdd2.derivee_func(func2, 0.1, 3.926), 2.0) 
        self.assertEqual(tdd2.derivee_func(func3, 1, 10), 2) 
        self.assertEqual(tdd2.derivee_func(func4, 0.001, 1.2*math.pi), -0.588)


if __name__ == '__main__':
    unittest.main()
