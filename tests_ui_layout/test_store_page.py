import standard
import login_page
import store_page
import re
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_to_cart(set_up) -> None:
    page = set_up
    login_page.login(set_up, 'standard_user','secret_sauce')
    expect(page.get_by_role("button", name="REMOVE").nth(0)).to_be_hidden
    expect(page.get_by_role("button", name="ADD TO CART").nth(5)).to_be_visible
    store_page.add_to_cart(set_up, 0)
    expect(page.get_by_role("button", name="REMOVE").nth(0)).to_be_visible
    expect(page.get_by_role("button", name="ADD TO CART").nth(5)).to_be_hidden
    expect(page.get_by_role("button", name="REMOVE").nth(1)).to_be_hidden
    expect(page.get_by_role("button", name="ADD TO CART").nth(4)).to_be_visible
    expect(page.locator("#shopping_cart_container")).to_contain_text('1')
    store_page.add_to_cart(set_up, 4)
    expect(page.get_by_role("button", name="REMOVE").nth(1)).to_be_visible
    expect(page.get_by_role("button", name="ADD TO CART").nth(4)).to_be_hidden
    expect(page.locator("#shopping_cart_container")).to_contain_text('2')


def test_remove_from_cart(set_up) -> None:
    page = set_up
    login_page.login(set_up, 'standard_user','secret_sauce')
    expect(page.get_by_role("button", name="REMOVE").nth(0)).to_be_hidden
    expect(page.locator("#shopping_cart_container")).to_be_empty()
    store_page.add_to_cart(set_up, 0)
    expect(page.locator("#shopping_cart_container")).to_contain_text('1')
    expect(page.get_by_role("button", name="REMOVE").nth(0)).to_be_visible
    store_page.remove_from_cart(set_up, 0)
    expect(page.get_by_role("button", name="REMOVE").nth(0)).to_be_hidden
    expect(page.locator("#shopping_cart_container")).to_be_empty()
    store_page.add_to_cart(set_up, 0)
    store_page.add_to_cart(set_up, 0)
    store_page.add_to_cart(set_up, 0)
    expect(page.locator("#shopping_cart_container")).to_contain_text('3')


def test_check_cart_details(set_up) -> None:
    page = set_up
    login_page.login(set_up, 'standard_user','secret_sauce')
    store_page.add_to_cart(set_up, 0)
    store_page.add_to_cart(set_up, 0)
    store_page.add_to_cart(set_up, 0)
    store_page.check_cart(set_up, '3')
    expect(page.locator("#cart_contents_container")).to_contain_text("DESCRIPTION")
    expect(page.locator("#cart_contents_container")).to_contain_text("CHECKOUT")
    expect(page.locator("#contents_wrapper")).to_contain_text("Your Cart")
    expect(page.locator("#shopping_cart_container")).to_contain_text('3')
    store_page.remove_from_cart(set_up, 0)
    expect(page.locator("#shopping_cart_container")).to_contain_text('2')


def test_page_layout_store_page(set_up) -> None:
    page = set_up
    login_page.login(set_up, 'standard_user','secret_sauce')
    standard.check_standard_fields(set_up)
    page.wait_for_load_state("networkidle")
    expect(page.locator("div").filter(has_text=re.compile(r"^ProductsName \(A to Z\)Name \(Z to A\)Price \(low to high\)Price \(high to low\)$")).first).to_be_visible()
    expect(page.locator("#header_container div").nth(1)).to_be_visible()
    expect(page.get_by_role("combobox")).to_be_visible()
    expect(page.locator("div:nth-child(6)")).to_be_visible()
    expect(page.locator("#item_4_title_link")).to_contain_text("Sauce Labs Backpack")
    expect(page.locator("#item_0_title_link")).to_contain_text("Sauce Labs Bike Light")
    expect(page.locator("#item_1_title_link")).to_contain_text("Sauce Labs Bolt T-Shirt")
    expect(page.locator("#item_3_title_link")).to_contain_text("Test.allTheThings() T-Shirt (Red)")
    expect(page.locator("#contents_wrapper")).to_contain_text("$9.99")
    expect(page.locator("div:nth-child(6) > .pricebar > .btn_primary")).to_be_visible()


