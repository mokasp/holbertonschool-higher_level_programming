#!/usr/bin/python3
""" unittest for Base """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBase(unittest.TestCase):
    """ testing base """

    def setUp(self):
        """ set up test """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ tear down test """
        pass

    def test_Start(self):
        """ simple base creation checking id"""
        self.base_1 = Base()
        self.assertEqual(self.base_1.id, 1)

    def test_Conseq(self):
        """ checking consqueative id """
        self.base_1 = Base()
        self.base_2 = Base()
        self.base_3 = Base()
        self.assertEqual(self.base_1.id, 1)
        self.assertEqual(self.base_2.id, 2)
        self.assertEqual(self.base_3.id, 3)

    def test_Random(self):
        """ check random id"""
        self.base_1 = Base(4)
        self.base_2 = Base(2)
        self.base_3 = Base(8)
        self.assertEqual(self.base_1.id, 4)
        self.assertEqual(self.base_2.id, 2)
        self.assertEqual(self.base_3.id, 8)

    def test_ConseqAndRandom(self):
        """ check mix of conseque and random """
        self.base_1 = Base()
        self.base_2 = Base(50)
        self.base_3 = Base()
        self.assertEqual(self.base_1.id, 1)
        self.assertEqual(self.base_2.id, 50)
        self.assertEqual(self.base_3.id, 2)

    # tests for tast 15 To Json String
    def test_toJsonstringOutput_Normal(self):
        """ correctt output of to_json_string """
        self.r1 = Rectangle(10, 7, 2, 8)
        dictionary = self.r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        output = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]'
        self.assertEqual(json_dictionary, output)

    def test_toJsonstringType(self):
        """ check output type """
        self.r1 = Rectangle(10, 7, 2, 8)
        dictionary = self.r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)

    def test_toJsonstringNone(self):
        """ check return if none passed """
        self.r1 = Rectangle(10, 7, 2, 8)
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_savetoFile(self):
        """ save to file normal output """
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        Rectangle.save_to_file([self.r1, self.r2])

        with open("Rectangle.json", "r") as file:
            rd = file.read()

        output = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10},\
 {"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]'
        self.assertEqual(rd, output)
