
import unittest

class TestStringMethods(unittest.TestCase):
    def test_negative(self):
        test_value = [1,4,5,2,4]
        a = 25
        message = "El valor a no esta en el itrerable"
        self.assertIn(a, test_value, message)

    def test_positive(self):
        test_value = [1,4,5,2,4]
        a = 2
        message = "El valor esta en el itrerable"
        self.assertIn(a, test_value, message)

if __name__ == '__main__':
    unittest.main()
