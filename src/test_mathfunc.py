#-*-coding:utf-8-*-

import unittest
from mathfunc import *


class TestMathFunc(unittest.TestCase):
    '''Test mathfunc.py'''

    def test_add(self):
        '''Test method add(a, b)'''
        self.assertEqual(add(3, 5), 8)
        self.assertNotEqual(add(1, 3), 3)


    def test_minus(self):
        '''Test method minus(a, b)'''
        self.assertEqual(minus(5, 1), 4)

    def test_multi(self):
        '''Test method multi(a, b)'''
        self.assertEqual(mulit(2, 5), 10)


    def test_divide(self):
        '''Test method divide(a, b)'''
        self.assertNotEqual(divide(9, 3), 2)


if __name__ == '__main__':
    unittest.main()

