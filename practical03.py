from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Edge()

# ================================================================================

file_path = os.path.abspath("index.html")
driver.get("file:///" + file_path)
driver.maximize_window()
time.sleep(3)

# ================================================================================

driver.find_element(By.ID, "nav-login").click()
driver.find_element(By.ID, "login-user").send_keys("Maazx")
driver.find_element(By.ID, "login-pass").send_keys("maaz@33221")
time.sleep(3)

# ================================================================================

if driver.find_element(By.ID, "login-submit").is_enabled():
    driver.find_element(By.ID, "login-submit").click()
else:
    print("Submit button is not enabled.")
    time.sleep(3)

# ================================================================================

driver.close()