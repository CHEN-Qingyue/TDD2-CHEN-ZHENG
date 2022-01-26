import tdd2
import unittest

class Test(unittest.TestCase):

    def test_miroir(self):
        self.assertEqual(tdd2.miroir('abcdefg',3),'abcddcba')
        self.assertEqual(tdd2.miroir('miroir',2),'mirrim')
        self.assertEqual(tdd2.miroir('12345',4),'1234554321')
        self.assertEqual(tdd2.miroir('pog',0),'pp')

 
    def test_derivee(self):
        self.assertEqual(tdd2.derivee([-2.979,-1.056,0.76,2.298,4.987],2),[0.96,0.91,0.77,1.34])
        self.assertEqual(tdd2.derivee([5.029,2.498,1.409,1.409,2.409,5.209],0.5),[-5.06,-2.18,0.0,2.0,5.6])
        self.assertEqual(tdd2.derivee([2.575,2.575,2.575,2.575],1),[0,0,0])
        self.assertEqual(tdd2.derivee([1],2),-1)
        
    
    def test_derivee2(self):
        self.assertEqual(tdd2.derivee2([-2.979,-1.056,0.76,2.298,4.987],2),[-0.02,-0.07,0.29])
        self.assertEqual(tdd2.derivee2([5.029,2.498,1.409,1.409,2.409,5.209],0.5),[5.76,4.36,4.0,7.2])
        self.assertEqual(tdd2.derivee2([2.575,2.575,2.575,2.575],1),[0,0])
        self.assertEqual(tdd2.derivee2([1,2],2),-1)

if __name__ == '__main__':
    unittest.main()
