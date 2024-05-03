from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

figure = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
print(figure)
