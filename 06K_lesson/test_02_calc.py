from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestSlowCalculator(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.wait = WebDriverWait(self.driver, 60)
        # Увеличенный таймаут ожидания

    def tearDown(self):
        self.driver.quit()

    def test_calculator(self):
        wait = self.wait

        # 1. Вводим значение 45 в поле #delay
        delay_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
            )
        delay_input.clear()
        delay_input.send_keys("45")

        # 2. Нажимаем кнопки: 7 → + → 8 → =
        # Кнопка 7
        wait.until(
            EC.element_to_be_clickable
            ((By.XPATH, "//span[text()='7']"))).click()
        # Кнопка +
        wait.until(EC.element_to_be_clickable
                   ((By.XPATH, "//span[text()='+']"))).click()
        # Кнопка 8
        wait.until(EC.element_to_be_clickable
                   ((By.XPATH, "//span[text()='8']"))).click()
        # Кнопка =
        wait.until(EC.element_to_be_clickable
                   ((By.XPATH, "//span[text()='=']"))).click()

        # 3. Ждём появления результата (до 45+ секунд с запасом)
        wait.until(
            EC.text_to_be_present_in_element
            ((By.CSS_SELECTOR, ".screen"), "15"),
            message="Результат не появился за отведённое время"
        )


if __name__ == "__main__":
    unittest.main()
