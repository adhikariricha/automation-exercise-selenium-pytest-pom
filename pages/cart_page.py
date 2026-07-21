from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    cart = (By.XPATH, "//a[@href='/view_cart']")

    def open_cart(self):
        self.scroll_to(self.cart)
        self.click(self.cart)