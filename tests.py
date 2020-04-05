import unittest
from color import Color


class TestColors(unittest.TestCase):
    def setUp(self):
        self.red = Color(1,0,0)
        self.green = Color(0,1,0)
        self.blue = Color(0,0,1)

    def test_convert(self):
        self.assertEqual(getattr(self.red.convert(), "r"), 255.0)
        self.assertEqual(getattr(self.green.convert(), "g"), 255.0)
        self.assertEqual(getattr(self.blue.convert(), "b"), 255.0)

    def test_addition(self):
        yellow = self.red + self.green
        white = self.red + self.green + self.blue
        self.assertEqual(getattr(yellow.convert(), "r"), 255.0)
        self.assertEqual(getattr(yellow.convert(), "g"), 255.0)
        self.assertEqual(getattr(yellow.convert(), "b"), 0)
        self.assertEqual(white.convert().r, 255)
    def test_multiplication(self):
        special = self.red.mult("r", .001)
        self.assertEqual(special.convert().r, 0)
if __name__ == "__main__":
    unittest.main()
