# In working


from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert




driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

# =================================================================================

driver.get("https://workspace.google.com/intl/en-US/gmail/")
driver.maximize_window()
# driver.implicitly_wait(10)

# =================================================================================




driver.close()












