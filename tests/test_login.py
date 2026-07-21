from pages.home_page import HomePage
from pages.login_page import LoginPage
from config.config import EMAIL, PASSWORD


def test_login(driver):

    home = HomePage(driver)
    home.click_signup()

    login = LoginPage(driver)

    login.login(EMAIL, PASSWORD)