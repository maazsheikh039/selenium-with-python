from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Firefox()

# =================================================================================

driver.get("https://workspace.google.com/intl/en-US/gmail/")
driver.maximize_window()
driver.implicitly_wait(10)

# =================================================================================

driver.find_element(By.XPATH, "/html/body/div[1]/gws-header/header/div/div[3]/span[3]/a/span").click()
# time.sleep(15)
driver.find_element(By.ID, "identifierId").send_keys("automation20068@gmail.com")
# time.sleep(5)
driver.find_element(By.NAME, 'V67aGc').click()



driver.close()












