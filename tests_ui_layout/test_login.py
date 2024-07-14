import login_page
import re
import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize("username",  ["standard_user",
                                             pytest.param("locked_out_user", marks=pytest.mark.xfail),
                                             "problem_user",
                                             'performance_glitch_user'])
@pytest.mark.parametrize("password", ['secret_sauce',
                                             pytest.param("fas", marks=pytest.mark.xfail),
                                             pytest.param("", marks=pytest.mark.xfail)])
def test_login(set_up, username, password) -> None:
    page = set_up
    login_page.login(set_up,username, password)
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="LOGIN")).to_be_hidden()
    expect(page.get_by_text("carry.allTheThings() with the")).to_be_visible()
    expect(page.locator("#header_container div").nth(1)).to_be_visible()
    expect(page.get_by_text("Products")).to_be_visible()
    expect(page.get_by_role("combobox")).to_be_visible()
    expect(page.get_by_role("combobox")).to_contain_text(
        "Name (A to Z)Name (Z to A)Price (low to high)Price (high to low)")