from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Получаем значение x и считаем y
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # Вводим ответ
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Кликаем чекбокс и радиокнопку
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажимаем кнопку
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

    # Успеваем посмотреть результат
    time.sleep(10)

finally:
    browser.quit()

# Закрываем браузер
browser.quit()