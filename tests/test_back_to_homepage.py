from pages.home_page import HomePage
from pages.discovery_page import DiscoveryPage

def test_logo_returns_home(setup_playwright):
    page = setup_playwright
    home = HomePage(page)
    home.select_city()

    DiscoveryPage(page).click_logo()
    home.expect_home_visible()
