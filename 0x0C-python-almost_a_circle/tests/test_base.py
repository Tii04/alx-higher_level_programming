#!/usr/bin/python3
""" This module has all of the unittests
    For base class"""


import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """
    Tests output of Base class"""

    def test_id(self):
        """ Tests id's from Base class"""

        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
