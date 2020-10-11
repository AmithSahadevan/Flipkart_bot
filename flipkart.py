from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.flipkart.com")

try:
    close = WebDriverWait(driver, 100).until(
        lambda x: x.find_element_by_xpath("/html/body/div[2]/div/div/button")
    )
    close.click()

    search = WebDriverWait(driver, 100).until(
        lambda x: x.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
    )
    search.send_keys("macbook air")
    search.send_keys(Keys.RETURN)


    linkclick = WebDriverWait(driver, 100).until(
        lambda x: x.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[3]/div/div/div/a")
    )
    linkclick.click()

except:
    driver.quit()