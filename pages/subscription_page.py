from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SubscriptionPage(BasePage):

    email = (By.ID, "susbscribe_email")
    button = (By.ID, "subscribe")

    def subscribe(self, email):

        # Scroll to the bottom of the page
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        # Enter email
        self.type(self.email, email)

        # Click Subscribe
        self.click(self.button)