from re import U
import unittest

class MyTestCase(unittest.TestCase):
    def test_one(self):
        pass

    def notatest(self):
        pass
    
    def test_two(self):
        pass

if __name__ == '__main__':
    unittest.main()

# Los tests se definen agregando  test al inicio  si no lo agregamos no ejecutara