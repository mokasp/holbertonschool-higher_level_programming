#!/usr/bin/python3
""" unittest for Base """
import unittest
from models.base import Base
import json

class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        pass

    def test_Start(self):
        self.base_1 = Base()
        self.assertEqual(self.base_1.id, 1)

    def test_Conseq(self):
        self.base_1 = Base()
        self.base_2 = Base()
        self.base_3 = Base()
        self.assertEqual(self.base_1.id, 1)
        self.assertEqual(self.base_2.id, 2)
        self.assertEqual(self.base_3.id, 3)

    def test_Random(self):
        self.base_1 = Base(4)
        self.base_2 = Base(2)
        self.base_3 = Base(8)
        self.assertEqual(self.base_1.id, 4)
        self.assertEqual(self.base_2.id, 2)
        self.assertEqual(self.base_3.id, 8)

    def test_ConseqAndRandom(self):
        self.base_1 = Base()
        self.base_2 = Base(50)
        self.base_3 = Base()
        self.assertEqual(self.base_1.id, 1)
        self.assertEqual(self.base_2.id, 50)
        self.assertEqual(self.base_3.id, 2)
