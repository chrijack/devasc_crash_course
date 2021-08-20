import unittest
from areacircle import area_of_circle
from math import pi

class Test_Area_of_Circle_input(unittest.TestCase):
    def test_area(self):
        # Test radius >= 0
        self.assertAlmostEqual(area_of_circle(1), pi)
        self.assertAlmostEqual(area_of_circle(0), 0)
        self.assertAlmostEqual(area_of_circle(3.5), pi * 3.5**2)

    def test_values(self):
        # Test that bad values are caught
        self.assertRaises(ValueError, area_of_circle, -1)

if __name__ == '__main__': 
    unittest.main() 