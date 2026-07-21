from pages.contact_page import ContactPage


def test_contact(driver):

    contact = ContactPage(driver)

    contact.open_contact()

    contact.fill_form()

    contact.submit_form()

    # Verify Contact Us page is still open after submission
    assert "contact_us" in driver.current_url