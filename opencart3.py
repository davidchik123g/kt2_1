import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService())


def register_test(driver):
    driver.get("https://demo-opencart.ru/index.php")

    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container div.nav.pull-right ul.list-inline li.dropdown:nth-child(2) > "
                                 "a.dropdown-toggle")

    search.click()

    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container div.nav.pull-right ul.list-inline li.dropdown.open:nth-child(2) "
                                 "ul.dropdown-menu.dropdown-menu-right li:nth-child(1) > a:nth-child(1)")

    search.click()

    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR, "#input-firstname")

    words = "Да"

    search.click()
    for letter in words:
        search.send_keys(letter)

    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR, "#input-lastname")

    words = "Га"

    search.click()
    for letter in words:
        search.send_keys(letter)

    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR, "#input-email")

    words = "gaga@gmail.com"

    search.click()
    for letter in words:
        search.send_keys(letter)

    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR, "#input-telephone")

    words = "12345"

    search.click()
    for letter in words:
        search.send_keys(letter)

    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR, "#input-password")

    words = "9999"

    search.click()
    for letter in words:
        search.send_keys(letter)

    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR, "#input-confirm")

    words = "9999"

    search.click()
    for letter in words:
        search.send_keys(letter)

    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container:nth-child(4) div.row div.col-sm-9 form.form-horizontal:nth-child(3) div.buttons:nth-child(4) div.pull-right > input:nth-child(3)")

    search.click()

    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container:nth-child(4) div.row div.col-sm-9 form.form-horizontal:nth-child(3) div.buttons:nth-child(4) div.pull-right > input.btn.btn-primary:nth-child(4)")

    search.click()

    time.sleep(2)


register_test(driver)
