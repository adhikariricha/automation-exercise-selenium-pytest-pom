from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_cart(driver):

    product = ProductsPage(driver)

    # Open Products page
    product.open_products()

    # Open first product
    product.open_first_product()

    # Add product to cart
    product.add_to_cart()

    # Continue Shopping
    product.continue_shopping()

    # Open Cart
    cart = CartPage(driver)
    cart.open_cart()

    # Verify Cart page opened
    assert "view_cart" in driver.current_url