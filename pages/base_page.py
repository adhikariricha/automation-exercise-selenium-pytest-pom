from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

  
    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

  

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()



    def type(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)


    def scroll_to(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

   

    def js_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

   

    def close_popup_if_present(self):
        try:
            close_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[text()='Close']")
                )
            )
            close_button.click()
            print("Advertisement popup closed successfully.")

        except TimeoutException:
            print("No advertisement popup found.")