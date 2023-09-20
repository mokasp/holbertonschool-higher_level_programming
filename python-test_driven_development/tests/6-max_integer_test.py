#!/usr/bin/python3
""" Documentation """

import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        list = [3, 4, 5]
        self.assertEqual(max_integer(list), 5)


if __name__ == "__main__":
    unittest.main()
