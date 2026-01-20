from pages.home_page import HomePage
from pages.discovery_page import DiscoveryPage

def test_city_shows_3_categories(setup_playwright):
    page = setup_playwright
    home = HomePage(page)
    home.select_city()

    discovery = DiscoveryPage(page)
    discovery.expect_categories(["Restaurants", "Groceries", "Alcohol"])
