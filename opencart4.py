import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService())


def search_test(driver):
    driver.get("https://demo-opencart.ru/index.php")

    search = driver.find_element(By.CSS_SELECTOR, "div.container div.row div.col-sm-5 div.input-group > "
                                                  "input.form-control.input-lg")

    words = "камеры"

    search.click()
    for letter in words:
        search.send_keys(letter)

    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR, "div.container div.row div.col-sm-5 div.input-group "
                                                  "span.input-group-btn > button.btn.btn-default.btn-lg")

    search.click()

    time.sleep(2)


search_test(driver)
