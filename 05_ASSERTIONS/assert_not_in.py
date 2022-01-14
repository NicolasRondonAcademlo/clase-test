
import unittest

class TestStringMethods(unittest.TestCase):
    def test_negative(self):
        test_value = [1,4,5,2,4]
        a = 2
        message = "El valor a  esta en el itrerable"
        self.assertNotIn(a, test_value, message)

    def test_positive(self):
        test_value = [1,4,5,2,4]
        a = 243
        message = "El valor no esta en el itrerable"
        self.assertNotIn(a, test_value, message)

if __name__ == '__main__':
    unittest.main()
