import pytest

def test_example(faker):
    num = faker.random_int()
    assert num == num
