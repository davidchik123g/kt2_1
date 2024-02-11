import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService())


def cart_test(products):
    driver.get("https://demo-opencart.ru/index.php")

    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(2) div.product-thumb.transition div.button-group > button:nth-child(1)")

    search.click()

    time.sleep(3)

    search1 = driver.find_element(By.CSS_SELECTOR,
                                  "div.container div.nav.pull-right ul.list-inline li:nth-child(4) a:nth-child(1) > i.fa.fa-shopping-cart")

    search1.click()

    time.sleep(2)

    products = driver.find_elements(By.CSS_SELECTOR, ".table-bordered tr")
    if len(products) <= 1:
        print("Корзина пуста.")
    else:
        print("Корзина не пуста.")

    driver.quit()


cart_test(driver)
