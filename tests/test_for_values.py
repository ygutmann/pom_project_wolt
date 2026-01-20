from pages.home_page import HomePage
from pages.discovery_page import DiscoveryPage
from pages.restaurants_page import RestaurantsPage

def test_restaurants_have_values(setup_playwright):
    page = setup_playwright
    home = HomePage(page)
    home.select_city()

    DiscoveryPage(page).open_category("Restaurants")
    RestaurantsPage(page).expect_has_at_least(2)
