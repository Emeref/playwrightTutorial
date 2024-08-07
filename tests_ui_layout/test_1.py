# import os
# import re
# import pytest
# from playwright.sync_api import Playwright, sync_playwright, expect
#
#
# PASSWORD = os.environ['PASSWORD']
#
#
# # try:
# #     PASSWORD = os.environ['PASSWORD']
# # except:
# #     import secret
# #     PASSWORD = secret.PASSWORD
# # @pytest.mark.skip
# @pytest.mark.parametrize("email",  ["standard_user",
#                                              pytest.param("test", marks=pytest.mark.xfail),
#                                              pytest.param("locked_out_user", marks=pytest.mark.xfail)])
# @pytest.mark.parametrize(" password", [PASSWORD,
#                                              pytest.param("fas", marks=pytest.mark.xfail)])
# def test_run3(set_up, email, password) -> None:
#     page = set_up
#     page.wait_for_load_state("networkidle")
#     page.get_by_text("Accepted usernames are: standard_user locked_out_user problem_user").click()
#     page.get_by_text("Accepted usernames are: standard_user locked_out_user problem_user").click()
#     page.locator("[data-test=\"username\"]").click()
#     page.locator("[data-test=\"username\"]").fill(email)
#     page.locator("[data-test=\"username\"]").press("Tab")
#     page.locator("[data-test=\"password\"]").fill(password)
#     page.locator("[data-test=\"password\"]").press("Tab")
#     page.get_by_role("img").click()
#     page.locator(".login_logo").click(timeout=1000)
#     page.get_by_role("button", name="LOGIN").click(timeout=1000)
#     expect(page).to_have_title("Swag Labs",timeout=1000)
#     expect(page.get_by_role("link", name="1")).to_be_hidden(timeout=1000)
#     page.locator("div").filter(has_text=re.compile(r"^\$29\.99ADD TO CART$")).get_by_role("button").click(timeout=1430)
#     expect(page.get_by_role("link", name="1")).to_be_visible()
#     expect(page.get_by_text("$15.99").nth(0)).to_be_visible()
#     expect(page.get_by_text("$15.99").nth(1)).to_be_visible()
#     page.get_by_role("link", name="1").click()
#     expect(page.get_by_role("link", name="1")).to_be_visible()
#     page.get_by_role("link", name="Continue Shopping").click()
#     page.wait_for_load_state("networkidle")
#     expect(page.get_by_role("button", name="LOGIN")).to_be_hidden()
#     assert page.get_by_role("button", name="LOGIN").is_hidden()
#
#     # ---------------------
#
