from playwright.sync_api import expect

class DiscoveryPage:
    CATEGORY_TITLE = '[data-test-id="ProductLine.Title"]'
    LOGO_LINK = "[data-test-id='HeaderWoltLogoLink']"

    def __init__(self, page):
        self.page = page

    def expect_category_visible(self, name: str, timeout: int = 30000):
        titles = self.page.locator(self.CATEGORY_TITLE)
        expect(titles.filter(has_text=name)).to_be_visible(timeout=timeout)

    def expect_categories(self, names: list[str], timeout: int = 30000):
        for n in names:
            self.expect_category_visible(n, timeout=timeout)

    def open_category(self, name: str):
        self.page.locator(self.CATEGORY_TITLE).filter(has_text=name).first.click()

    def click_logo(self):
        self.page.locator(self.LOGO_LINK).click()
