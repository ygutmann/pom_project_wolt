from playwright.sync_api import expect

class RestaurantsPage:
    RESTAURANT_LINKS = 'a[href*="/restaurant/"]'

    def __init__(self, page):
        self.page = page

    def expect_has_at_least(self, n: int, timeout: int = 30000):
        items = self.page.locator(self.RESTAURANT_LINKS)

        # מחכים שלפחות אחד נטען
        expect(items.first).to_be_visible(timeout=timeout)

        # ואז בודקים כמות
        assert items.count() >= n, f"Expected at least {n} restaurants, got {items.count()}"
