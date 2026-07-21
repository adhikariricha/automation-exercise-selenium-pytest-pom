from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    email = (By.XPATH, "//input[@data-qa='login-email']")
    password = (By.XPATH, "//input[@data-qa='login-password']")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")

    def enter_email(self, user):
        self.type(self.email, user)

    def enter_password(self, pwd):
        self.type(self.password, pwd)

    def click_login(self):
        self.click(self.login_button)

    def login(self, user, pwd):
        self.enter_email(user)
        self.enter_password(pwd)
        self.click_login()