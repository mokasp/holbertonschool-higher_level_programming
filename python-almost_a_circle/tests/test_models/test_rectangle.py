#!/usr/bin/python3
""" unittest for Rectangle """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ testing rectangle """

    def setUp(self):
        """ set up test object """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ tear down test object """
        pass

    def test_createRectangle(self):
        """ simple rectangle creation """
        self.rect_1 = Rectangle(2, 3)
        self.assertEqual(self.rect_1.id, 1)
        self.assertEqual(self.rect_1.width, 2)
        self.assertEqual(self.rect_1.height, 3)

    def test_createRectangle2(self):
        """ more complex rectangle creation """
        self.rect_1 = Rectangle(3, 3, 1, 2, 12)
        self.assertEqual(self.rect_1.id, 12)
        self.assertEqual(self.rect_1.width, 3)
        self.assertEqual(self.rect_1.height, 3)
        self.assertEqual(self.rect_1.x, 1)
        self.assertEqual(self.rect_1.y, 2)

    def test_widthSetter(self):
        """ check if width sets """
        self.rect_1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(self.rect_1.id, 1)
        self.assertEqual(self.rect_1.width, 1)
        self.assertEqual(self.rect_1.height, 1)
        self.assertEqual(self.rect_1.x, 1)
        self.assertEqual(self.rect_1.y, 1)
        self.rect_1.width = 2
        self.assertEqual(self.rect_1.width, 2)

    def test_ConseqId(self):
        """ check if ids are consequtive """
        self.rect_1 = Rectangle(2, 3)
        self.rect_2 = Rectangle(2, 3)
        self.rect_3 = Rectangle(2, 3)
        self.assertEqual(self.rect_1.id, 1)
        self.assertEqual(self.rect_2.id, 2)
        self.assertEqual(self.rect_3.id, 3)
