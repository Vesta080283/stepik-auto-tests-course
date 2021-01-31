import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# webdriverChromeOptions: Options = webdriver.ChromeOptions()
# webdriverChromeOptions.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
# driverBinaryLocation = "C:\\DEVEL\\Repositories\\Selenium\\WebDriver\\chrome_87.0.4280.88_x86\\chromedriver.exe"
link = "http://suninjuly.github.io/registration2.html"

try:
    # browser = webdriver.Chrome(driverBinaryLocation, chrome_options = webdriverChromeOptions)
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector(
        ".first_block .form-group.first_class input.first")
    first_name.send_keys("Test")
    last_name = browser.find_element_by_css_selector(
        ".first_block .form-group.second_class input.second")
    last_name.send_keys("Test")
    email = browser.find_element_by_css_selector(
        ".first_block .form-group.third_class input.third")
    email.send_keys("test@test.tst")
    phone = browser.find_element_by_css_selector(
        ".second_block .form-group.first_class input.first")
    phone.send_keys("555-5555")
    address = browser.find_element_by_css_selector(
        ".second_block .form-group.second_class input.second")
    address.send_keys("Test St. 1")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
