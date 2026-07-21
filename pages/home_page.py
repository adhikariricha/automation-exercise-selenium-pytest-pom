from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):

    logo = (By.XPATH, "//img[@alt='Website for automation practice']")
    signup = (By.LINK_TEXT, "Signup / Login")

    def verify_home_page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.logo)
        ).is_displayed()

    def click_signup(self):
        self.scroll_to(self.signup)
        self.click(self.signup)