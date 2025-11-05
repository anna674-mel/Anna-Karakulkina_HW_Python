from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Неявное ожидание (10 секунд)
driver.implicitly_wait(10)
driver.get("http://uitestingplayground.com/textinput")

# Нахождение поля ввода и ввод текста "SkyPro"
input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")

# Нахождение синей кнопки и нажатие на неё
blue_button = driver.find_element(By.CSS_SELECTOR, "button#updatingButton")
blue_button.click()

# Ожидание изменения текста кнопки (явное ожидание)
updated_button = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, "button#updatingButton"), "SkyPro")
    )

# Получение актуального текста кнопки
button_text = blue_button.text

# Вывод текста кнопки в консоль
print(button_text)

driver.quit()
