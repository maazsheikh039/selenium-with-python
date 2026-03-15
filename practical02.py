from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

# ============================================================

file_path = os.path.abspath("index.html")
driver.get("file:///" + file_path)
driver.maximize_window()
time.sleep(3)

# ============================================================

driver.find_element(By.ID, "nav-signup").click()

try:
    username = driver.find_element(By.ID, "reg-user").send_keys("maazheikh039")
    email = driver.find_element(By.ID, "reg-email").send_keys("maazheikh039@gmail.com")
    password = driver.find_element(By.ID, "reg-pass").send_keys("maaz@321")
    time.sleep(3)
except Exception as e:
    print("An error occurred:", e)

# ============================================================

if driver.find_element(By.ID, "reg-submit").is_enabled():
    driver.find_element(By.ID, "reg-submit").click()
else:
    print("Submit button is not enabled.")

# ============================================================

driver.close()
