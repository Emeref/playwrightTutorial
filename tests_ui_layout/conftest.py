import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def set_up (page) -> None:
    # browser = playwright.chromium.launch(headless=False )
    # context = browser.new_context()
    # page = context.new_page()
    page.set_default_timeout(10000)
    page.goto("https://www.saucedemo.com/v1/index.html")

    yield page