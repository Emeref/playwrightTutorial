import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run3(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False )
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(10000)
    page.goto("https://www.saucedemo.com/v1/index.html")
    page.wait_for_load_state("networkidle")
    page.get_by_text("Accepted usernames are: standard_user locked_out_user problem_user").click()
    page.get_by_text("Accepted usernames are: standard_user locked_out_user problem_user").click()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").press("Tab")
    page.get_by_role("img").click()
    page.locator(".login_logo").click(timeout=1000)
    page.get_by_role("button", name="LOGIN").click(timeout=1000)
    expect(page).to_have_title("Swag Labs",timeout=1000)
    expect(page.get_by_role("link", name="1")).to_be_hidden(timeout=1000)
    page.locator("div").filter(has_text=re.compile(r"^\$29\.99ADD TO CART$")).get_by_role("button").click(timeout=1430)
    expect(page.get_by_role("link", name="1")).to_be_visible()
    expect(page.get_by_text("$15.99").nth(0)).to_be_visible()
    expect(page.get_by_text("$15.99").nth(1)).to_be_visible()
    page.get_by_role("link", name="1").click()
    expect(page.get_by_role("link", name="1")).to_be_visible()
    page.get_by_role("link", name="Continue Shopping").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="LOGIN")).to_be_hidden()
    assert page.get_by_role("button", name="LOGIN").is_hidden()

    # ---------------------
    context.close()
    browser.close()

