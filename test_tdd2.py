import tdd2
import unittest

class Test(unittest.TestCase):

    def test_min_int(self):
        self.assertEqual(tdd2.miroir('abcdefg',3),'abcddcba')
        self.assertEqual(tdd2.miroir('miroir',2),'mirrim')
        self.assertEqual(tdd2.miroir('12345',4),'1234554321')
        self.assertEqual(tdd2.miroir('pog',0),'pp')

 

if __name__ == '__main__':
    unittest.main()
