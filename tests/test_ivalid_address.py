from pages.home_page import HomePage, expect

def test_invalid_city_shows_no_addresses(setup_playwright):
    page = setup_playwright
    home = HomePage(page)

    home.select_city()
    search = page.get_by_placeholder("Enter delivery address")
    search.fill("ghghghhghgh")



