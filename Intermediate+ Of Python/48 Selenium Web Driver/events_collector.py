from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org/")

event_dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_title = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

# events = {i+1: {"date": value,"name": value for value in event_dates} for (i) in range(len(event_dates))}
# print(event_title.text)
driver.close()
