#!/usr/bin/python3
""" Documentation """

import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):

    def test_maxend(self):
        list = [3, 4, 5]
        self.assertEqual(max_integer(list), 5)
    
    def test_maxbegin(self):
        list = [5, 3, 4]
        self.assertEqual(max_integer(list), 5)
    
    def test_maxmiddle(self):
        list = [3, 5, 4]
        self.assertEqual(max_integer(list), 5)
    
    def test_maxneg(self):
        list = [3, -4, 5]
        self.assertEqual(max_integer(list), 5)
    
    def test_maxend(self):
        list = [-3, -4, -5]
        self.assertEqual(max_integer(list), -3)
    
    def test_maxone(self):
        list = [3]
        self.assertEqual(max_integer(list), 3)
    
    def test_maxempty(self):
        list = []
        self.assertEqual(max_integer(list), None)


if __name__ == "__main__":
    unittest.main()
