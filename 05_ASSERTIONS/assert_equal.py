import unittest

class TestStringMethod(unittest.TestCase):

    def test_negative(self):
        first_value = "Hola"
        second_value = "Mundo"
        message = "El primer valor y el segundo valor son diferentes"
        self.assertEqual(first_value, second_value, message)


class TestStringMethodWorks(unittest.TestCase):
    
    def test_positive(self):
        first_value = "Hola"
        second_value = "Hola"
        message = "Primer y segundo valor son iguales"
        self.assertEqual(first_value, second_value, message)

if __name__ == '__main__':
    unittest.main()