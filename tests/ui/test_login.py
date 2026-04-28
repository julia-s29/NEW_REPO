from playwright.sync_api import Page


def test_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    assert page.locator("#flash").is_visible()
    assert "You logged into a secure area!" in page.locator("#flash").text_content()