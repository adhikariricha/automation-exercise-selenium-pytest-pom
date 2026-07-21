from pages.products_page import ProductsPage


def test_search_product(driver):

    product = ProductsPage(driver)

    product.open_products()

    product.search_product("Summer White Top")