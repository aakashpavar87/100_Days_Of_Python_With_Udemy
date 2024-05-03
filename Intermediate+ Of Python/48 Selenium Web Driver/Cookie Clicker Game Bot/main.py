import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

tools = driver.find_elements(By.CSS_SELECTOR, "div.grayed")
# tool1 = driver.find_elements(By.XPATH, '//*[@id="buyCursor"]/b/text()[2]')
for tool in tools:
    print(tool[1].text)

# timeout = time.time() + 120
# while True:
#     test = 0
#     if test == 5 or time.time() > timeout:
#         break;
#     cookie.click()
#     money = driver.find_element(By.ID, "money").text
#     for price in tools:
#         pass
#     test -= 1

cps = driver.find_element(By.ID, "cps").text
driver.quit()

print(cps)

