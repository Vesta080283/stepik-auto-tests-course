from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    input1 = browser.find_element_by_id("input_value")
    x = input1.text
    y = calc(x)

    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
