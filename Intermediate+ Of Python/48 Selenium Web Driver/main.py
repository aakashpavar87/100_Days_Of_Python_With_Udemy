from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_driver_path = "C:\\Development\\new_driver\\chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
browser.get("https://www.amazon.in/dp/B09WQYFLRX?ref_=cm_sw_r_cp_ud_dp_JVVCB9MXJVVV79F7DAHM")
name = browser.find_element(By.ID, "productTitle").text
# price = browser.find_element(By.CSS_SELECTOR, "a-accordion-row-a11y "
#                                             "a-accordion-row a-declarative accordion-header mobb-header-css")
price = browser.find_element(By.XPATH,
                              '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]'
                             ).text
print(f"{name} \n{int(price.replace(',', ''))}")
browser.close()

