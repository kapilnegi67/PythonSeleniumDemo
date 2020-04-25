import arithmetic_functions as AF
import pytest
import platform


@pytest.mark.One
@pytest.mark.Sanity
def test_addition():
    assert AF.addition(2, 3) == 5


@pytest.mark.One
@pytest.mark.Smoke
def test_multiplication():
    assert AF.multiplication(2, 3) == 6


@pytest.mark.Two
@pytest.mark.Smoke
def test_subtraction():
    assert AF.subtraction(3, 2) == 1


@pytest.mark.Two
@pytest.mark.Sanity
def test_division():
    assert AF.division(4, 2) == 2


@pytest.mark.skipif(platform.system().lower()=="darwin", reason="Test not supported on Mac os")
# @pytest.mark.skip(reason="Skipping Testcase at will")
def test_skipif_example():
    print("This should not get printed on Mac os")

# skip
# skipif
