import re
from playwright.sync_api import expect

class CareersPage:
    def __init__(self, page):
        self.page = page

    def expect_loaded(self, timeout: int = 15000):
        expect(self.page).to_have_url(re.compile(r"careers\.wolt\.com"), timeout=timeout)
