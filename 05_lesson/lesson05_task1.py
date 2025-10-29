from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
print(driver.title)
sleep(3)
driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
sleep(5)
driver.quit()
