from pages.products_page import ProductsPage


def test_view_product(driver):

    product = ProductsPage(driver)

    # Open Products page
    product.open_products()

    # Open first product
    product.open_first_product()

    # Verify Product Details page opened
    assert "product_details" in driver.current_url