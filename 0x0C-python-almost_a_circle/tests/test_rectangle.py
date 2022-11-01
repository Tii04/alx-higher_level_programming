#!/usr/bin/python3

""" Module that tests rectangle.py"""


from models.rectangle import Rectangle
import unittest


class test_rectangle(unittest.TestCase):
    """ Class tests functionality of
    rectangle.py"""

    def test_rectangles(self):
        """ Method with test cases"""

        if __name__ == "__main__":

            r1 = Rectangle(10, 2)
            r2 = Rectangle(2, 10)
            r3 = Rectangle(10, 2, 0, 0, 12)

            self.assertEqual(r1.id, 1)
            self.assertEqual(r2.id, 2)
            self.assertEqual(r1.id, 12)

    def test_area(self):
        """ Tests the area method"""

        if __name__ == "__main__":

            r1 = Rectangle(3, 2)
            r2 = Rectangle(2, 10)
            r3 = Rectangle(8, 7, 0, 0, 12)

            self.assertEqual(r1, 6)
            self.assertEqual(r2, 20)
            self.assertEqual(r3, 56)
