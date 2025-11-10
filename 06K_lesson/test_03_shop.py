from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestSauceDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_purchase_flow(self):
        wait = self.wait

        # 1. Авторизация
        username_input = wait.until(EC.presence_of_element_located
                                    ((By.ID, "user-name")))
        username_input.send_keys("standard_user")

        password_input = wait.until(EC.presence_of_element_located
                                    ((By.ID, "password")))
        password_input.send_keys("secret_sauce")

        login_button = wait.until(EC.element_to_be_clickable
                                  ((By.ID, "login-button")))
        login_button.click()

        # 2. Добавление товаров в корзину
        # Sauce Labs Backpack
        backpack = wait.until(EC.element_to_be_clickable(
            ((By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Backpack']]//button[text()='Add to cart']")))
        )
        backpack.click()

        # Sauce Labs Bolt T-Shirt
        tshirt = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Bolt T-Shirt']]//button[text()='Add to cart']")))
        tshirt.click()

        # Sauce Labs Onesie
        onesie = wait.until(EC.element_to_be_clickable
                            ((By.XPATH, "//div[@class='inventory_item' and .//div[text()='Sauce Labs Onesie']]//button[text()='Add to cart']")))
        onesie.click()

        # 3. Переход в корзину
        cart_link = wait.until(EC.element_to_be_clickable
                               ((By.CLASS_NAME, "shopping_cart_link")))
        cart_link.click()

        # 4. Нажатие Checkout
        checkout_button = wait.until(EC.element_to_be_clickable
                                     ((By.ID, "checkout")))
        checkout_button.click()

        # 5. Заполнение формы
        first_name_input = wait.until(EC.presence_of_element_located
                                      ((By.ID, "first-name")))
        first_name_input.send_keys("Иван")

        last_name_input = wait.until(EC.presence_of_element_located
                                     ((By.ID, "last-name")))
        last_name_input.send_keys("Иванов")

        zip_code_input = wait.until(EC.presence_of_element_located
                                    ((By.ID, "postal-code")))
        zip_code_input.send_keys("123456")

        # Нажатие Continue
        continue_button = wait.until(EC.element_to_be_clickable
                                     ((By.ID, "continue")))
        continue_button.click()


if __name__ == "__main__":
    unittest.main()
