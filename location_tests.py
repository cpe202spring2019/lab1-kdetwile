import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr1(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_repr2(self):
        loc = Location("SL", 35, -120)
        self.assertEqual(repr(loc),"Location('SL', 35, -120)")

    def test_repr3(self):
        loc = Location("SLO County", 88.9, -120.7)
        self.assertEqual(repr(loc),"Location('SLO County', 88.9, -120.7)")

    def test_repr4(self):
        loc = Location("Alaska", 0.8, -12.7)
        self.assertEqual(repr(loc),"Location('Alaska', 0.8, -12.7)")
    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
