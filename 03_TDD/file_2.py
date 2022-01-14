import unittest

# TDD
def addition(arg1, arg2):
    return arg1 +arg2

class AdditioonTestCase(unittest.TestCase):
    def test_main(self):
        result = addition(3,2)
        assert result == 5

if __name__ == '__main__':
    unittest.main()
