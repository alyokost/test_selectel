from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://my.selectel.ru/login"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_id('login')
    input1.send_keys("лаблбла")
    input2 = browser.find_element_by_id('password')
    input2.send_keys("Password")

    button = browser.find_element_by_css_selector("button.m-solid")
    button.click()

    error_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[stl=err_login]"))
        )

    assert error_element.text == 'Неправильный логин или пароль'
    print('Тест пройден')
    
finally:
    
    time.sleep(5)
   # закрываем браузер
    browser.quit()

