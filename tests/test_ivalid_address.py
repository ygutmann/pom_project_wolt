from pages.home_page import HomePage, expect

def test_invalid_city_shows_no_addresses(setup_playwright):
    page = setup_playwright
    home = HomePage(page)

    search = page.get_by_placeholder("Enter delivery address")
    search.click()
    search.fill("ghghghghgh")



