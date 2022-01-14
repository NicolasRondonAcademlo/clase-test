
from tkinter.messagebox import NO
import unittest

class TestStringMethods(unittest.TestCase):
    def test_negative(self):
        a = None
        message = "El valor a  es None"
        self.assertIsNotNone(a, message)

    def test_positive(self):
        a = 34
        message = "El valor a no es None"
        self.assertIsNotNone(a, message)



if __name__ == '__main__':
    unittest.main()
