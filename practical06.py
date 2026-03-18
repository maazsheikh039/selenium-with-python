import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()

# ===============================================

driver.get("https://github.com/maazsheikh039")
t.sleep(1)
driver.maximize_window()
t.sleep(2)

# ===============================================

github_edit_button = driver.find_element(By.XPATH, '//*[@id="user-profile-frame"]/div/div[1]/div/article/div[1]/h1')
driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border:2px solid red;');", github_edit_button)
t.sleep(5)

# ===============================================

def take_screenshot(driver, os):                
    my_path = os.getcwd() + "\\"
    file_name = my_path + t.asctime().replace(":", "_") + ".png"
    driver.save_screenshot(file_name)

take_screenshot(driver, os)

# ===============================================

driver.quit()
    