from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LogoutPage(BasePage):

    logout = (By.XPATH, "//a[@href='/logout']")

    def logout_user(self):
        self.scroll_to(self.logout)
        self.click(self.logout)