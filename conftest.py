import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():

    options = Options()

    # Start browser maximized
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )


    driver.implicitly_wait(10)

   
    driver.get("https://automationexercise.com")

    yield driver

   
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        if "driver" in item.funcargs:

            driver = item.funcargs["driver"]

            os.makedirs("screenshots", exist_ok=True)

            test_name = item.name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            filename = f"{test_name}_{timestamp}.png"

            driver.save_screenshot(
                os.path.join("screenshots", filename)
            )