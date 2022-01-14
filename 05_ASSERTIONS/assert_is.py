
import unittest

class TestStringMethods(unittest.TestCase):
    def test_negative(self):
        a = 1
        b = "z"
        message = "El valor a no es b"
        self.assertIs(a,b, message)

    def test_positive(self):
        a = 1
        b = 1
        message = "El valor a es b"
        self.assertIs(a,b, message)



if __name__ == '__main__':
    unittest.main()
