from audioop import add
from cgitb import reset
import unittest

# TDD
def addition(*args):
    total = 0 
    for a in args:
        total += a
    return total 

class AdditioonTestCase(unittest.TestCase):
    def test_three_args(self):
        result = addition(3,2, 1)
        assert result == 6

    def test_no_args(self):
        result = addition()
        assert result == 0
        
if __name__ == '__main__':
    unittest.main()