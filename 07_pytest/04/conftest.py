import pytest

@pytest.fixture(scope="session", autouse=True)
def set_up_suite():
    print("START TEST")
    yield
    print("Finished Test")