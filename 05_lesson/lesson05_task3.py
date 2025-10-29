
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()  # Убедитесь, что geckodriver установлен

driver.get("http://the-internet.herokuapp.com/inputs")

input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )

input_field.send_keys("Sky")
sleep(2)
input_field.clear()

input_field.send_keys("Pro")
sleep(2)
driver.quit()
