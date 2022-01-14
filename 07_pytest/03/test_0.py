import pytest

@pytest.mark.usefixtures("provide_current_time")
class TestMultiple:
    def test_first(self):
        print("Running AT", self.now)
        assert 5 == 5

    @pytest.mark.usefixtures("greetings")
    def test_second(self):
        assert 10 == 10


@pytest.fixture
def greetings():
    print("hello")
    yield
    print("Goodbye")


@pytest.fixture(scope="class")
def provide_current_time(request):
    import datetime
    request.cls.now = datetime.datetime.utcnow()
    print("Enter Cls")
    yield
    print("Exit Cls")