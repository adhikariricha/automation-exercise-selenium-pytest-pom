from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):

    products = (By.XPATH, "//a[@href='/products']")
    search_box = (By.ID, "search_product")
    search_button = (By.ID, "submit_search")

    view_product = (By.XPATH, "(//a[text()='View Product'])[1]")

    add_cart = (By.XPATH, "//button[@type='button']")

    continue_btn = (By.XPATH, "//button[text()='Continue Shopping']")

    def open_products(self):
        self.click(self.products)

    def search_product(self, product):
        self.type(self.search_box, product)
        self.click(self.search_button)

    def open_first_product(self):
        self.scroll_to(self.view_product)
        self.click(self.view_product)

    def add_to_cart(self):
        self.scroll_to(self.add_cart)
        self.click(self.add_cart)

    def continue_shopping(self):
        self.click(self.continue_btn)