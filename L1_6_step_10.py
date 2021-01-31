from selenium import webdriver
from time import sleep


def main(driver):
    try:
        driver.get("http://suninjuly.github.io/registration2.html")

        driver.find_element_by_css_selector(
            "div.first_class > input[required]").send_keys("some_text")
        driver.find_element_by_css_selector(
            "div.second_class > input[required]").send_keys("some_text")
        driver.find_element_by_css_selector(
            "div.third_class > input[required]").send_keys("some_text")

        send_button = driver.find_element_by_css_selector("button.btn")
        send_button.click()

        sleep(1)

        reg_text = driver.find_element_by_css_selector("h1")
        assert reg_text.text == "Congratulations! You have successfully registered!"
    finally:
        sleep(10)
        driver.quit()


if __name__ == "__main__":
    _driver = webdriver.Chrome()
    main(_driver)
