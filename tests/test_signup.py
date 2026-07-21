from pages.home_page import HomePage
from pages.signup_page import SignupPage

from config.config import NAME

from config.config import PASSWORD


def test_signup(driver):

    home = HomePage(driver)
    home.click_signup()

    signup = SignupPage(driver)
    signup.signup(NAME, PASSWORD)

    # Verify account creation page
    assert "account_created" in driver.current_url