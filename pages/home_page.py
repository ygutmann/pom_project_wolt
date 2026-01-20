from playwright.sync_api import expect

class HomePage:
    url = "https://wolt.com/en/isr"
    address_button = "#_R_tdj_"
    address_input_placeholder = "Enter delivery address"
    logo_link = "[data-test-id='HeaderWoltLogoLink']"

    def __init__(self, page: object) -> None:
        self.page = page

    def open(self):
        self.page.goto(self.url)


    def select_city(self):
        search = self.page.get_by_placeholder("Enter delivery address")
        search.click()
        search.fill("Jerusalem")
        expect(self.page.locator('[role="option"]').first).to_be_visible(timeout=10000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")


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

    def expect_no_addresses_found(self, timeout: int = 10000):
        expect(self.get_by_text("No addresses found")).to_be_visible()
