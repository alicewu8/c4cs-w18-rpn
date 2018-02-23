# python standard library module
import unittest

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



