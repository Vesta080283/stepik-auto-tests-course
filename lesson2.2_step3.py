from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(num1, num2):
    return str(num1 + num2)


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_id("num1")
    num1 = int(element1.text)
    element2 = browser.find_element_by_id("num2")
    num2 = int(element2.text)

    y = calc(num1, num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
