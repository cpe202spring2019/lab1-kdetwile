import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """list is equal to None and a ValueError should be raised"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter1(self):
        """Max number in list is 8, function should return 8"""
        tlist = [1, 2, 3, 4, 8]
        self.assertEqual(max_list_iter(tlist), 8)

    def test_max_list_iter2(self):
        """empty list is entered and function should return None"""
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_max_list_iter3(self):
        """Single item list, should return only item"""
        tlist = [7]
        self.assertEqual(max_list_iter(tlist), 7)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec1(self):
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_reverse_rec2(self):
        self.assertEqual(reverse_rec([4, 6, 8, 10]),[10, 8, 6, 4])

    def test_reverse_rec3(self):
        self.assertEqual(reverse_rec([1]),[1])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search4(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = 10
        self.assertEqual(bin_search(4, 0, 10, list_val), 4 )

    def test_bin_search1(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = 10
        self.assertEqual(bin_search(7, 0, 10, list_val), 5 )

    def test_bin_search2(self):
        list_val =[3,4,8,9,10]
        low = 3
        high = 10
        self.assertEqual(bin_search(7, 3, 10, list_val), None )

    def test_bin_search3(self):
        list_val = None
        low = 0
        high = 10
        self.assertEqual(bin_search(7, 0, 10, list_val), ValueError)

if __name__ == "__main__":
        unittest.main()