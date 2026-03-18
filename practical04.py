from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

# ========================================================

driver.get("https://github.com/maazsheikh039")
driver.maximize_window()
time.sleep(3)

# ========================================================

total_height = driver.execute_script("return document.body.offsetHeight;")
total_width = driver.execute_script("return document.body.offsetWidth;")
print("Total Height:", total_height)
print("Total Width:", total_width)

driver.set_window_size(total_width, total_height)
time.sleep(3)

# ========================================================

# textarea = driver.find_element(By.ID, "APjFqb")

h1_head_github = driver.find_element(By.XPATH, '//*[@id="user-profile-frame"]/div/div[1]/div/article/div[1]/h1')
h2_head_github = driver.find_element(By.XPATH, '//*[@id="user-profile-frame"]/div/div[1]/div/article/div[3]/h3')
# ========================================================

driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border:2px solid red;');", h1_head_github)
driver.execute_script("arguments[0].setAttribute('style', 'background: red; border:2px solid blue;');", h2_head_github)
time.sleep(5)

# =================================== --ScreenShots-- ===================================

def take_screenshot(driver, my_path):
    my_path = os.getcwd() + "\\"
    file_name = my_path + time.asctime().replace(":", "_") + ".png"
    driver.save_screenshot(file_name)

take_screenshot(driver, os)
# ========================================================

# driver.save_screenshot("google_homepage.png")
# driver.get_screenshot_as_file("new-raddif.png")
# print(driver.get_screenshot_as_png())

driver.close()