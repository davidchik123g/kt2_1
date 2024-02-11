import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService())

def screenshot_test(driver):

    driver.get("https://demo-opencart.ru/index.php")

    search = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(4) div.product-thumb.transition div.caption h4:nth-child(1) > a:nth-child(1)")

    search.click()

    time.sleep(2)

    search1 = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row div.col-sm-8 ul.thumbnails li:nth-child(1) > a.thumbnail")

    search1.click()

    time.sleep(2)


    search2 = driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-s-ready.mfp-image-holder > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close:nth-child(4)")

    search2.click()

    time.sleep(2)

    search3 = driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-s-ready.mfp-image-holder > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close:nth-child(4)")

    search3.click()

    time.sleep(2)

    search4 = driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-s-ready.mfp-image-holder > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close:nth-child(4)")

    search4.click()

    time.sleep(2)

    driver.quit()

screenshot_test(driver)