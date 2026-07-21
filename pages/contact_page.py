from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ContactPage(BasePage):

    contact = (By.XPATH, "//a[@href='/contact_us']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    subject = (By.NAME, "subject")
    message = (By.ID, "message")
    submit = (By.NAME, "submit")

    def open_contact(self):
        self.click(self.contact)

    def fill_form(self):
        self.type(self.name, "Richa")
        self.type(self.email, "richa@gmail.com")
        self.type(self.subject, "Internship Testing")
        self.type(
            self.message,
            "This is an automation testing project."
        )

    def submit_form(self):
        self.scroll_to(self.submit)
        self.click(self.submit)

        # Handle confirmation alert
        WebDriverWait(self.driver, 10).until(
            EC.alert_is_present()
        )

        self.driver.switch_to.alert.accept()