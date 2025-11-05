from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

driver.get
("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ожидание 3-х изображений
WebDriverWait(driver, 20).until(
        lambda d: len(d.find_elements
                      (By.CSS_SELECTOR, "#image-container img")) >= 3
    )
# Нахождение 3 картинки из списка
images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
print(f"Успешно найдено {images[2].get_attribute("src")}")

driver.quit()
