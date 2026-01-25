import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def setup_playwright():
    with sync_playwright() as p:

        headless = os.getenv("CI", "false").lower() == "true"
        browser = p.chromium.launch(headless=headless)

        context = browser.new_context()
        page = context.new_page()


        page.set_default_timeout(60_000)

        page.goto("https://wolt.com/en/isr", wait_until="domcontentloaded")
        page.wait_for_load_state("networkidle")

        yield page

        context.close()
        browser.close()
