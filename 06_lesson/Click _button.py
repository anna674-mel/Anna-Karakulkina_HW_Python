from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Неявное ожидание (20 секунд)
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/ajax")

# Нахождение и нажатие на синюю кнопку
button = driver.find_element(By.XPATH, "//button[@id='ajaxButton']")
button.click()

# Ожидание появления зелёной плашки с текстом (явное ожидание)
green_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )
# Получение текста из зелёной плашки
text_from_alert = green_alert.text

# Вывод текста в консоль
print(text_from_alert)

driver.quit()
