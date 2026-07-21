from pages.home_page import HomePage


def test_home(driver):

    home = HomePage(driver)

    assert home.verify_home_page()