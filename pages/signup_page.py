from datetime import datetime
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupPage(BasePage):

    # Signup form
    name = (By.NAME, "name")
    email = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_btn = (By.XPATH, "//button[@data-qa='signup-button']")

    # Account Information
    gender = (By.ID, "id_gender2")      # Mrs
    password = (By.ID, "password")

    # Address Information
    first_name = (By.ID, "first_name")
    last_name = (By.ID, "last_name")
    address = (By.ID, "address1")
    state = (By.ID, "state")
    city = (By.ID, "city")
    zipcode = (By.ID, "zipcode")
    mobile = (By.ID, "mobile_number")

    create_account = (By.XPATH, "//button[@data-qa='create-account']")

    def signup(self, name, password):
        unique_email = f"{name.lower()}{datetime.now().strftime('%Y%m%d%H%M%S')}@yopmail.com"
        print(f"Generated Email: {unique_email}")

        # Signup
        self.type(self.name, name)
        self.type(self.email, unique_email)
        self.click(self.signup_btn)

        # Account Information
        self.click(self.gender)
        self.type(self.password, password)

        # Address Information
        self.type(self.first_name, "Prabha")
        self.type(self.last_name, "Adhikari")
        self.type(self.address, "Kathmandu")
        self.type(self.state, "Bagmati")
        self.type(self.city, "Kathmandu")
        self.type(self.zipcode, "44600")
        self.type(self.mobile, "9800000000")

        # Scroll to Create Account button
        self.scroll_to(self.create_account)

        # Create Account
        self.click(self.create_account)