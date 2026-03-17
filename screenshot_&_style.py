from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# ========================================================

driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(3)

# ========================================================
textarea = driver.find_element(By.ID, "APjFqb")
# ========================================================

driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border:2px solid red;');", textarea)
time.sleep(10)


# =================================== --ScreenShots-- ===================================

# driver.save_screenshot("google_homepage.png")
# driver.get_screenshot_as_file("new-raddif.png")
# print(driver.get_screenshot_as_png())

driver.close()