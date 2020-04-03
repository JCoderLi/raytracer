import unittest
from vector import Vector

class TestVectors(unittest.TestCase):
    def setUp(self):
         self.v1 = Vector(1.0, -2.0, -2.0)
         self.v2 = Vector(3.0, 6.0, 9.0)
    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3.0)

    def normalize():
        self.assertEqual(self.v1.normalize(), )

    def test_addition(self):
        addition = self.v1 + self.v2
        self.assertEqual(getattr(addition, "x"), 4.0)

    def test_subtraction(self):
        subtraction = self.v1 - self.v2
        self.assertEqual(getattr(subtraction, "x"), -2.0)

    def test_division(self):
        division = self.v1 / 3
        self.assertEqual(getattr(division, "x"), 1.0/3)

    def test_multiplication(self):
        multiplication = self.v1 * 3
        rmultiplication = 3 * self.v1
        self.assertEqual(getattr(multiplication, "x"), 1.0 * 3)
        self.assertEqual(getattr(multiplication, "x"), 1.0 * 3)

if __name__ == "__main__":
    unittest.main()
