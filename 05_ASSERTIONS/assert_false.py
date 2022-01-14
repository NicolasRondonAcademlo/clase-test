
import unittest

class TestStringMethods(unittest.TestCase):
    def test_negative(self):
        test_value = True
        message = "El valor no es falso"
        self.assertFalse(test_value, message)

    def test_positive(self):
        test_value = False
        message = "El valor  es falso"
        self.assertFalse(test_value, message)


if __name__ == '__main__':
    unittest.main()
