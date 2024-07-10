import pytest
from playwright.sync_api import Playwright
import os

PASSWORD = os.environ['PASSWORD']
# try:
#     PASSWORD = os.environ['PASSWORD']
# except:
#     import secret
#     PASSWORD = secret.PASSWORD



@pytest.fixture
def set_up (page) -> None:
    # browser = playwright.chromium.launch(headless=False )
    # context = browser.new_context()
    # page = context.new_page()
    page.set_default_timeout(10000)
    page.goto("https://www.saucedemo.com/v1/index.html")

    yield page
    page.close()

@pytest.fixture
def login_set_up(set_up):
    page = set_up
    page.wait_for_load_state("networkidle")
    page.get_by_text("Accepted usernames are: standard_user locked_out_user problem_user").click()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill(PASSWORD)
    page.locator("[data-test=\"password\"]").press("Tab")
    page.get_by_role("img").click()
    page.locator(".login_logo").click(timeout=1000)
    page.get_by_role("button", name="LOGIN").click(timeout=1000)

    yield page