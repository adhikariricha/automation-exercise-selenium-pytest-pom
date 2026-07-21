# E-Commerce Website Automation Testing

## Project Overview

This project automates the testing of the AutomationExercise e-commerce website using Selenium WebDriver with Python. The framework follows the Page Object Model (POM) design pattern and uses Pytest for test execution and reporting.

Website Tested:
https://automationexercise.com/

---

## Objectives

- Automate major functionalities of the website.
- Reduce manual testing effort.
- Implement the Page Object Model (POM).
- Generate HTML test reports.
- Capture screenshots on test failure.
- Perform performance testing.

---

## Tools & Technologies

- Python 3.14
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Google Chrome
- ChromeDriver
- Visual Studio Code
- webdriver-manager

---

## Project Structure

ecommerce website/

├── config/

│ └── config.py

├── pages/

│ ├── base_page.py

│ ├── home_page.py

│ ├── signup_page.py

│ ├── login_page.py

│ ├── products_page.py

│ ├── contact_page.py

│ └── logout_page.py

├── tests/

│ ├── test_signup.py

│ ├── test_login.py

│ ├── test_products.py

│ ├── test_view_product.py

│ ├── test_cart.py

│ ├── test_contact.py

│ ├── test_logout.py

│ └── test_performance.py

├── reports/

├── screenshots/

├── conftest.py

├── pytest.ini

├── requirements.txt

└── README.md

---

## Test Cases Implemented

- Homepage Verification
- User Signup
- User Login
- Product Search
- View Product
- Add Product to Cart
- Contact Us Form
- User Logout
- Performance Testing

---

## Selenium Locators Used

- ID
- Name
- XPath
- Link Text

---

## Dynamic Content Handling

Explicit Wait (WebDriverWait) was used to handle dynamic web elements before interacting with them.

---

## Features

- Page Object Model (POM)
- Pytest Framework
- HTML Test Report
- Screenshot Capture on Failure
- Explicit Waits
- Reusable Code Structure

---

## Performance Testing

Homepage load time was measured during automation execution.

Expected Load Time:
Less than 5 seconds

Actual Load Time:
Approximately 6.3 seconds

---

## Bug Found
A functional bug was identified during the automation testing of the Automation Exercise website. The detailed bug report is available below:
https://docs.google.com/document/d/1LIut6c9TnjF150gdiGijRj7s3eSdumtabz0zyrzUWcs/edit?usp=sharing

---

## How to Run the Project

1. Install Python.

2. Install required packages:

pip install -r requirements.txt

3. Run all test cases:

pytest

4. Generate HTML report:

pytest --html=reports/report.html

---

## Test Results

| Test Category | Result |
|---------------|--------|
| Functional Testing | ✅ Passed |
| Performance Testing | ✅ Executed |
| HTML Report Generation | ✅ Generated |
| Bug Reporting | ✅ Completed |

## Author

Prabha Adhikari

B.Sc. CSIT
