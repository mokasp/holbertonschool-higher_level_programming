#!/usr/bin/python3
""" unittest for Square """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        pass

    def test_createSquare1(self):
        self.square_1 = Square(2)
        self.assertEqual(self.square_1.id, 1)
        self.assertEqual(self.square_1.size, 2)
        self.assertEqual(self.square_1.x, 0)
        self.assertEqual(self.square_1.y, 0)
    
    def test_createSquare2(self):
        self.square_1 = Square(3, 1, 2, 12)
        self.assertEqual(self.square_1.id, 12)
        self.assertEqual(self.square_1.size, 3)
        self.assertEqual(self.square_1.x, 1)
        self.assertEqual(self.square_1.y, 2)

    def test_createSquare3(self):
        self.square_1 = Square(1, 1, 1, 1)
        self.assertEqual(self.square_1.id, 1)
        self.assertEqual(self.square_1.size, 1)
        self.assertEqual(self.square_1.x, 1)
        self.assertEqual(self.square_1.y, 1)
        self.square_1.size = 2
        self.assertEqual(self.square_1.size, 2)

    def test_ConseqId(self):
        self.square_1 = Square(2)
        self.square_2 = Square(2)
        self.square_3 = Square(2)
        self.assertEqual(self.square_1.id, 1)
        self.assertEqual(self.square_2.id, 2)
        self.assertEqual(self.square_3.id, 3)
