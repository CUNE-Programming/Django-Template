from playwright import Page, expect
import pytest

pytestmark = pytest.mark.django_db

def test_example(page: Page):
    page.goto("google.com")
    expect(page).to_have_title("Google")