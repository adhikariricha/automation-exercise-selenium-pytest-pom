from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

from config.config import EMAIL, PASSWORD


def test_logout(driver):

    # Open Login Page
    home = HomePage(driver)
    home.click_signup()

    # Login
    login = LoginPage(driver)
    login.login(EMAIL, PASSWORD)

    # Logout
    logout = LogoutPage(driver)
    logout.logout_user()

    # Verify Logout Successful
    assert "login" in driver.current_url