
import unittest

class MyClass:
    x = 5

class Myclass2:
    x = 6

class TestStringMethods(unittest.TestCase):
    def test_negative(self):
        object_name = MyClass()
        message = "El objeto dado no es una isntancia de mi clase Myclass2"
        self.assertIsInstance(object_name, Myclass2, message)

    def test_positive(self):
        object_name = MyClass()
        message = "El objeto dado es isntancia de mi clase Myclass2"
        self.assertIsInstance(object_name, MyClass, message)

if __name__ == '__main__':
    unittest.main()
