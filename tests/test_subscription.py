from pages.subscription_page import SubscriptionPage


def test_subscription(driver):

    subscription = SubscriptionPage(driver)

    subscription.subscribe("richa@gmail.com")

    # Verify subscription section is displayed
    assert "Automation Exercise" in driver.title