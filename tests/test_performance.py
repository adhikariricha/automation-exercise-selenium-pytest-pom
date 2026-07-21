import time


def test_page_load(driver):

    url = "https://automationexercise.com"

    # Measure page load time
    start_time = time.perf_counter()

    driver.get(url)

    end_time = time.perf_counter()

    load_time = end_time - start_time

    print(f"\nWebsite: {url}")
    print(f"Page Load Time: {load_time:.2f} seconds")

    # Performance Check
    assert load_time < 5, (
        f"Performance Test Failed! "
        f"Page loaded in {load_time:.2f} seconds (Expected: < 5 seconds)"
    )