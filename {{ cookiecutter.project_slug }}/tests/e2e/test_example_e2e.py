from playwright.sync_api import Page, expect
import pytest

def test_example(page: Page):
    page.goto("https://google.com")
    expect(page).to_have_title("Google")
