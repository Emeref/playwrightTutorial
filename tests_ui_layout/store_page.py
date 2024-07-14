import re
from playwright.sync_api import Playwright, sync_playwright, expect

def add_to_cart(set_up, item_nr) -> None:
    page = set_up
    page.get_by_role("button", name="ADD TO CART").nth(item_nr).click()
    page.wait_for_load_state("networkidle")

def check_cart_value(set_up, nr_of_items) -> None:
    page = set_up
    expect(page.locator("#shopping_cart_container")).to_contain_text(nr_of_items)

def remove_from_cart(set_up, item_nr) -> None:
    page = set_up
    page.get_by_role("button", name="REMOVE").nth(item_nr).click()


def check_cart(set_up, nr_of_items) -> None:
    page = set_up
    page.get_by_role("link", name=nr_of_items).click()
    page.wait_for_load_state("networkidle")