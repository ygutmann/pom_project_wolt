from playwright.sync_api import expect

class HomePage:
    url = "https://wolt.com/en/isr"
    address_button = "#_R_tdj_"
    address_input_placeholder = "Enter delivery address"
    logo_link = "[data-test-id='HeaderWoltLogoLink']"

    def __init__(self, page: object) -> None:
        self.ADDRESS_INPUT_PLACEHOLDER = None
        self.page = page

    def open(self):
        self.page.goto(self.url)

    def select_city(self, city="Jerusalem"):
        page = self.page
        for name in ["Accept all", "Allow", "Accept"]:
            btn = page.get_by_role("button", name=name)
            if btn.count() > 0 and btn.first.is_visible():
                btn.first.click()
                break
        search = page.get_by_placeholder("Enter delivery address")
        expect(search).to_be_visible(timeout=60_000)
        search.click()
        search.fill(city)
        first_option = page.locator('[role="option"]').first
        expect(first_option).to_be_visible(timeout=60_000)
        first_option.click()
        page.keyboard.press("Escape")

    def expect_home_visible(self, timeout: int = 15000):
        expect(self.page.get_by_placeholder(self.address_input_placeholder)).to_be_visible(timeout=timeout)

    def click_jobs(self):
         self.page.get_by_role("link", name="Jobs").click()

    def click_logo(self):
        self.page.locator(self.logo_link).click()

    def type_city(self, text: str):

        self.page.locator("#_R_tdj_").click()
        search = self.page.get_by_placeholder(self.ADDRESS_INPUT_PLACEHOLDER)
        search.click()
        search.fill(text)

    def expect_no_addresses_found(self):
        expect(self.get_by_text("No addresses found")).to_be_visible()

    def get_by_text(self, param):
        pass
