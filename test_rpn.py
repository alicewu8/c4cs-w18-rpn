# for advanced homework 8: send in screenshots of calculations that fail and then tests that fix them

# python standard library module
import unittest

import operator

# import is similar to include in C++
import rpn

class TestBasics(unittest.TestCase): 
    
    # self parameter acts as this pointer: self should be the first member
    # of every member function in a class
    # self is analogous to dereferencing 'this' pointer
    def test_add(self): 
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def test_adds(self):
        result = rpn.calculate('1 1 + 2 +')
        self.assertEqual(4, result)
    def test_subtract(self):
        result = rpn.calculate('5 2 -')
        self.assertEqual(3, result)
    def test_toomany(self):
        # with expects to raise an error
        with self.assertRaises(TypeError):
            result = rpn.calculate('1 2 3 +')
    def test_manyadds(self):
        result = rpn.calculate('19 21 +')
        self.assertEqual(40, result);
    def test_pow(self):
        result = rpn.calculate('2 2 ^')
        self.assertEqual(4, result);
    def test_pow(self):
	result = rpn.calculate('2 0 ^')
	self.assertEqual(1, result);


