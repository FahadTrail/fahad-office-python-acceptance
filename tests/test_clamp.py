import unittest
from arithmetic import clamp


class ClampTests(unittest.TestCase):
    def test_below_range(self):
        self.assertEqual(clamp(1, 5, 10), 5)

    def test_in_range(self):
        self.assertEqual(clamp(7, 5, 10), 7)

    def test_above_range(self):
        self.assertEqual(clamp(12, 5, 10), 10)

    def test_exact_lower_boundary(self):
        self.assertEqual(clamp(5, 5, 10), 5)

    def test_exact_upper_boundary(self):
        self.assertEqual(clamp(10, 5, 10), 10)

    def test_invalid_bounds(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 5)


if __name__ == "__main__":
    unittest.main()
