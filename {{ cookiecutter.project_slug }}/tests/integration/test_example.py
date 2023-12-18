import pytest

pytestmark = pytest.mark.django_db

def test_example(faker):
    num = faker.random_int()
    assert num == num