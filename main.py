from main import *
import unittest

class Mytests(unittest.TestCase):
    def test_args(self):
        self.assertEqual(add(2, 2), 4)

    def test_kwargs(self):
        self.assertEqual(add(a=10, b=20), 30)

    def test_mixed(self):
        self.assertEqual(add(3, x=8), 11)

    def test_deef(self):
        x = 10
        y = 0
        self.assertEqual(add(0, -5, y, a=x), 5)

    def test_wrong_datatype(self):
        self.assertEqual(add("5", "abc", 10), 15)

if __name__ == "__main__":
    unittest.main()

class Mytests(unittest.TestCase):
    def test_args(self):
        self.assertEqual(minus(2, 2), -4)

    def test_kwargs(self):
        self.assertEqual(minus(a=5, b=2), -7)

    def test_mixed(self):
        self.assertEqual(minus(3, x=1), 2)

    def test_deef(self):
        x = 15
        y = 8
        self.assertEqual(minus(58, 5, y, a=x), -86)

    def test_wrong_datatype(self):
        self.assertEqual(minus("5", "abc", 10), -15)

if __name__ == "__main__":
    unittest.main()

class Mytests(unittest.TestCase):
    def test_args(self):
        self.assertEqual(multiply(2, 2), 0)

    def test_kwargs(self):
        self.assertEqual(multiply(a=5, b=2), 3)

    def test_mixed(self):
        self.assertEqual(multiply(3, x=1), 3)

    def test_deef(self):
        x = 1
        y = 2
        self.assertEqual(multiply(5, 5, y, a=x), 0)

    def test_wrong_datatype(self):
        self.assertEqual(multiply("5", "abc", 10), 50)

if __name__ == "__main__":
    unittest.main()

class Mytests(unittest.TestCase):
    def test_args(self):
        self.assertEqual(devide(2, 2), 1)

    def test_kwargs(self):
        self.assertEqual(devide(a=5, b=5), 1)

    def test_mixed(self):
        self.assertEqual(devide(3, x=1), 3)

    def test_deef(self):
        x = 1
        y = 2
        self.assertEqual(devide(10, 5, y, a=x), 1)

    def test_wrong_datatype(self):
        self.assertEqual(devide("50", "abc", 10), 0)

if __name__ == "__main__":
    unittest.main()
