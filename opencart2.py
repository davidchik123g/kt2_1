import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService())


def pcpage_test(driver):
    driver.get("https://demo-opencart.ru/index.php")

    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) > a.dropdown-toggle")

    search.click()

    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) div.dropdown-menu div.dropdown-inner ul.list-unstyled li:nth-child(1) > a:nth-child(1)")

    search.click()

    time.sleep(2)

    products = driver.find_elements(By.CSS_SELECTOR, ".product-layout")
    if not products:
        print("Страница категории PC пуста.")
    else:
        print("Страница категории PC не пуста.")

    driver.quit()


pcpage_test(driver)
