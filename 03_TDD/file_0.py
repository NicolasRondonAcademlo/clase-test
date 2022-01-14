import unittest

class SomeTestCase(unittest.TestCase):
    def test_something(self):
        # Arrange, nothing to prepare
        # Act phase, call do_something
        result = do_something() # noqa
        # Assert , verificamos que do_something() haga lo que esperamos
        assert result == "di something"



if __name__ == '__main__':
    unittest.main()