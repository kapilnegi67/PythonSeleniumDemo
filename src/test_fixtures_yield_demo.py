import pytest


@pytest.fixture()
def setup():
    print("Before Test")
    yield
    print("After Test")
    print("After Test2")


def test_tm1(setup):
    print("Test 1")


def test_tm2(setup):
    print("Test 2")


def test_tm3(setup):
    print("Test 3")
