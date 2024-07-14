# import re
#
# import pytest
# from playwright.sync_api import Playwright, sync_playwright, expect
#
# @pytest.mark.smoke
# # @pytest.mark.xfail(reason="Sprawdzam czy sie wywali")
#
# def test_start(login_set_up):
#     page = login_set_up
#
#     expect(page).to_have_title("Swag Labs",timeout=1000)
#     expect(page.get_by_role("link", name="1")).to_be_hidden(timeout=1000)
#     page.locator("div").filter(has_text=re.compile(r"^\$29\.99ADD TO CART$")).get_by_role("button").click(timeout=1430)
#
#     expect(page.get_by_role("link", name="1")).to_be_visible()
#     expect(page.get_by_text("$15.99").nth(0)).to_be_visible()
#     expect(page.get_by_text("$15.99").nth(1)).to_be_visible()
#     page.get_by_role("link", name="1").click()
#     expect(page.get_by_role("link", name="1")).to_be_visible()
#     page.get_by_role("link", name="Continue Shopping").click()
#     page.wait_for_load_state("networkidle")
#     expect(page.get_by_role("button", name="LOGIN")).to_be_hidden()
#     assert page.get_by_role("button", name="LOGIN").is_hidden()
#     text = page.get_by_text("Sauce Labs Backpackcarry.").text_content()
#
#     assert text != "da"
#     #
#     #
#     # # ---------------------
#     # context.close()
#     # browser.close()
# # @pytest.mark.skip(reason="bo tak")
# def test_start_2(login_set_up):
#     page = login_set_up
#     # page.wait_for_load_state("networkidle")
#     # page.get_by_text("Accepted usernames are: standard_user locked_out_user problem_user").click()
#     # page.get_by_text("Accepted usernames are: standard_user locked_out_user problem_user").click()
#     # page.locator("[data-test=\"username\"]").click()
#     # page.locator("[data-test=\"username\"]").fill("performance_glitch_user")
#     # page.locator("[data-test=\"username\"]").press("Tab")
#     # page.locator("[data-test=\"password\"]").fill("secret_sauce")
#     # page.locator("[data-test=\"password\"]").press("Tab")
#     # page.get_by_role("img").click()
#     # page.locator(".login_logo").click()
#     # page.get_by_role("button", name="LOGIN").click()
#     expect(page).to_have_title("Swag Labs")
#     expect(page.get_by_role("link", name="1")).to_be_hidden()
#     page.locator("div").filter(has_text=re.compile(r"^\$29\.99ADD TO CART$")).get_by_role("button").click()
#
#     expect(page.get_by_role("link", name="1")).to_be_visible()
#     expect(page.get_by_text("$15.99").nth(0)).to_be_visible()
#     expect(page.get_by_text("$15.99").nth(1)).to_be_visible()
#     page.get_by_role("link", name="1").click()
#     expect(page.get_by_role("link", name="1")).to_be_visible()
#     page.get_by_role("link", name="Continue Shopping").click()
#     page.wait_for_load_state("networkidle")
#     expect(page.get_by_role("button", name="LOGIN")).to_be_hidden()
#     assert page.get_by_role("button", name="LOGIN").is_hidden()
#     # # ---------------------
#     # context.close()
#     # browser.close()
#
#
