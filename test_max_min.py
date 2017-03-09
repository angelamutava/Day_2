import unittest
import find_max_min as testcases


class MaxMinTest(unittest.TestCase):
    """docstring for MaxMinTest"""

    """tests the max and min for the list provided"""
    def test_find_max_min_four(self):
        self.assertListEqual([1, 4],
                             testcases.find_max_min([1, 2, 3, 4]),
                             msg='should return [1,4] for [1, 2, 3, 4]')
    
    """tests the max and min for the list provided"""
    def test_find_max_min_one(self):
        self.assertListEqual([4, 6],
                             testcases.find_max_min([6, 4]),
                             msg='should return [4, 6] for [6, 4]')

     """tests the max and min for the list provided"""
    def test_find_max_min_two(self):
        self.assertListEqual([2, 78],
                             testcases.find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2]),
                             msg='should return [2, 78] for [4, 66, 6, 44, 7, 78, 8, 68, 2]')

    """tests the max and min for the list provided"""
    def test_find_max_min_three(self):
        self.assertListEqual([1, 4],
                             testcases.find_max_min([1, 2, 3, 4]),
                             msg='should return [1,4] for [1, 2, 3, 4]')

    """tests equality of max and min and returns the length of the list"""
    def test_find_max_min_identity(self):
        self.assertListEqual([4],
                             testcases.find_max_min([4, 4, 4, 4]),
msg='Return the number of elements in the list in a new list if the `min` and `max` are equal')