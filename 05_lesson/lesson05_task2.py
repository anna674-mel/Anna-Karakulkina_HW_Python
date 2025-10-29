from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

button = WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.XPATH,
                                 "//button[contains(@class, 'btn-primary')]"))
)
button.click()

sleep(3)

driver.quit()
