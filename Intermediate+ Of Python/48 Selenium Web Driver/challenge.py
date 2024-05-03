from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first = driver.find_element(By.NAME, "fName")
first.send_keys("Aakash")
second = driver.find_element(By.NAME, "lName")
second.send_keys("Pavar")
mail = driver.find_element(By.NAME, "email")
mail.send_keys("demomail@gmail.com")
btn = driver.find_element(By.TAG_NAME, "button")
btn.click()