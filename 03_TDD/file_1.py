# Probar que 3 +2 es 5
import unittest

# TDD

class AdditioonTestCase(unittest.TestCase):
    def test_main(self):
        result = addition(3,2)
        assert result == 5

if __name__ == '__main__':
    unittest.main()


# Al correr nuestro test este fallarara porque la funcion addition no esta definida