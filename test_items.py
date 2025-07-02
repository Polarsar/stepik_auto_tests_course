import time
from selenium.webdriver.common.by import By

def test_guest_should_see_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # для визуальной проверки языка кнопки

    add_to_cart_btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_cart_btn, "Кнопка добавления в корзину не найдена на странице товара"
