
from playwright.sync_api import Playwright, sync_playwright, expect

def check_standard_fields(set_up)-> None:
    page = set_up
    page.get_by_role("button", name="Open Menu").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("link", name="All Items")).to_be_visible()
    expect(page.locator("#header_container div").first).to_be_visible()
    expect(page.get_by_role("link", name="About")).to_be_visible()
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
    expect(page.get_by_text("Reset App State")).to_be_visible()
    expect(page.get_by_role("button", name="Close Menu")).to_be_visible()
    expect(page.get_by_text("All ItemsAboutLogoutReset App")).to_be_visible()
    page.locator(".bm-overlay").click()
    page.wait_for_load_state("networkidle")
    expect(page.locator("#header_container div").nth(1)).to_be_visible()
    expect(page.get_by_role("contentinfo").get_by_role("img")).to_be_visible()
    expect(page.get_by_text("LinkedIn")).to_be_visible()
    expect(page.get_by_text("Facebook")).to_be_visible()
    expect(page.get_by_text("Twitter")).to_be_visible()
    expect(page.get_by_text("© 2020 Sauce Labs. All Rights")).to_be_visible()
    expect(page.get_by_text("Twitter Facebook LinkedIn ©")).to_be_visible()
    expect(page.locator("#shopping_cart_container").get_by_role("link")).to_be_visible()


