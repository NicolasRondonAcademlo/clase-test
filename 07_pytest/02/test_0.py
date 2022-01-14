import pytest

@pytest.fixture
def greetings():
    print("hello")
    yield
    print("Goodbye")

class TestMultiple:
    def test_first(self):
        assert 5 == 5

    @pytest.mark.usefixtures("greetings")
    def test_second(self):
        assert 10 == 10