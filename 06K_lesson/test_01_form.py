from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_form_validation(self):
        driver = self.driver
        wait = self.wait

        # Заполняем форму
        wait.until(EC.presence_of_element_located
                   ((By.NAME, "first-name"))).send_keys("Иван")
        wait.until(EC.presence_of_element_located
                   ((By.NAME, "last-name"))).send_keys("Петров")
        wait.until(EC.presence_of_element_located
                   ((By.NAME, "address"))).send_keys("Ленина, 55-3")
        wait.until(EC.presence_of_element_located
                   ((By.NAME, "e-mail"))).send_keys("test@skypro.com")
        wait.until(EC.presence_of_element_located
                   ((By.NAME, "phone"))).send_keys("+7985899998787")
        # Zip code оставляем пустым
        wait.until(EC.presence_of_element_located
                   ((By.NAME, "zip-code"))).clear()
        wait.until(EC.presence_of_element_located
                   ((By.NAME, "city"))).send_keys("Москва")
        wait.until(EC.presence_of_element_located
                   ((By.NAME, "country"))).send_keys("Россия")
        wait.until(EC.presence_of_element_located
                   ((By.NAME, "job-position"))).send_keys("QA")
        wait.until(EC.presence_of_element_located
                   ((By.NAME, "company"))).send_keys("SkyPro")

        # Нажимаем Submit
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()

        # Проверяем стили полей после отправки
        # Zip code должен быть подсвечен красным
        zip_code_field = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
        self.assertTrue("alert-danger" in zip_code_field.get_attribute("class")),
        "Поле Zip code не подсвечено красным"

        # Остальные поля должны быть подсвечены зелёным
        valid_fields = [
            driver.find_element(By.ID, "first-name"),
            driver.find_element(By.ID, "last-name"),
            driver.find_element(By.ID, "address"),
            driver.find_element(By.ID, "e-mail"),
            driver.find_element(By.ID, "phone"),
            driver.find_element(By.ID, "city"),
            driver.find_element(By.ID, "country"),
            driver.find_element(By.ID, "job-position"),
            driver.find_element(By.ID, "company")
        ]

        for field in valid_fields:
            self.assertTrue("alert-success" in field.get_attribute("class"),
                            f"Поле {field.get_attribute
                                    ('id')} не подсвечено зелёным")


if __name__ == "__main__":
    unittest.main()
