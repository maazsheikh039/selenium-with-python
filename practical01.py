from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os



file_path = os.path.abspath("index.html")
driver = webdriver.Chrome()
driver.get("file:///" + file_path)
driver.maximize_window()

myusername = driver.find_element(By.ID, "login-user").send_keys("Maazx")
myuserpass = driver.find_element(By.ID, "login-pass").send_keys("password3212")
mylogin = driver.find_element(By.ID, "login-submit").click()

time.sleep(15)
driver.close()