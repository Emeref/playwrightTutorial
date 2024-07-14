

def login(set_up, username, password)-> None:
    page = set_up
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill(password)
    page.get_by_role("button", name="LOGIN").click()

