import arithmetic_functions as AF
import pytest

test_data = [[1, 2, 3],
             ["Hello", "World", "HelloWorld"],
             ]


@pytest.mark.parametrize("value1", "value2", "result", test_data)
def test_generic_add(value1, value2, result):
    assert AF.addition(value1, value2) == result
