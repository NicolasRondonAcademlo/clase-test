import unittest

class TestStringMethod(unittest.TestCase):

    def test_negative(self):
        first_value = "Hola"
        second_value = "Hola"
        message = "El primer valor y el segundo valor no son diferentes"
        self.assertNotEqual(first_value, second_value, message)

    def test_positive(self):
        first_value = "Mundo"
        second_value = "Hola"
        message = "El primer valor y el segundo valor son diferentes"
        self.assertNotEqual(first_value, second_value, message)

if __name__ == '__main__':
    unittest.main()
