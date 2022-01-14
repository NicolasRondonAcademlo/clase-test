import imp


import unittest
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("Antes")

    def test_one(self):
        pass

    def tearDown(self):
        print("Despues")

class MySecondTestCase(unittest.TestCase):
    def test_two_part_2(self):
        pass
    
    def test_two(self):
        pass



if __name__ == '__main__':
    unittest.main()