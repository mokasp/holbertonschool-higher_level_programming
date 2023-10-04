#!/usr/bin/python3
""" unittest for Base """
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        print("\nRunning setUp method...")
        self.base_1 = Base()
        self.base_2 = Base()
        self.base_3 = Base(12)
    def tearDown(self):
        print("Running tearDown method...")
    def test_id(self):
        print("Running Tests...")
        self.assertEqual(self.base_1.id, 1)
        self.assertEqual(self.base_2.id, 2)
        self.assertEqual(self.base_3.id, 12)

