
from tkinter.messagebox import NO
import unittest

class TestStringMethods(unittest.TestCase):
    def test_negative(self):
        a = "Es algo"
        message = "El valor a  no es None"
        self.assertIsNone(a, message)

    def test_positive(self):
        a = None
        message = "El valor a es None"
        self.assertIsNone(a, message)



if __name__ == '__main__':
    unittest.main()
