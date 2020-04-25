import pytest


@pytest.yield_fixture()
def setup():
    print("Before Test")
    yield
    print("After Test")


def test_tm1(setup):
    print("Test 1")


def test_tm2(setup):
    print("Test 2")


def test_tm3(setup):
    print("Test 3")
