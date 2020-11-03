from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://my.selectel.ru/login"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("a[stl=restore]").click()
    reset_element = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[stl=h1]"))
        )

    assert reset_element.text == 'Восстановление доступа'
    print('Тест пройден')
    
finally:
    
    time.sleep(5)
   # закрываем браузер
    browser.quit()
