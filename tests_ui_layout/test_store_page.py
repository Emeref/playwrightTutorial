import time

import login_page
import store_page
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

@pytest.mark.develop
def test_check_cart_details(set_up) -> None:
    page = set_up
    login_page.login(set_up, 'standard_user','secret_sauce')
    store_page.add_to_cart(set_up, 0)
    store_page.add_to_cart(set_up, 0)
    store_page.add_to_cart(set_up, 0)
    store_page.check_cart(set_up, '3')
    expect(page.locator("#cart_contents_container")).to_contain_text("DESCRIPTION")
    expect(page.locator("#cart_contents_container")).to_contain_text("CHECKOUT")
    # expect(page.get_by_role("class", name='subheader')).to_contain_text("Your Cart")
    expect(page.locator("#shopping_cart_container")).to_contain_text('3')
    store_page.remove_from_cart(set_up, 0)
    expect(page.locator("#shopping_cart_container")).to_contain_text('2')
