import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://wolt.com/en/isr"

@pytest.fixture(scope="session")
def setup_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1400, "height": 900})
        page = context.new_page()

        page.goto(BASE_URL)
        page.get_by_role("button", name="Allow").click()

        yield page

        context.close()
        browser.close()
