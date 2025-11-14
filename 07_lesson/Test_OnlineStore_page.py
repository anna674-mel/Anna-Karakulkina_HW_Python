import unittest
from selenium import webdriver
# Импортируйте классы страниц (если они в отдельных файлах)
from OnlineStorePage import LoginPage
from OnlineStorePage import InventoryPage
from OnlineStorePage import CartPage
from OnlineStorePage import CheckoutPage


class TestSauceDemo(unittest.TestCase):
    
    def setUp(self):
        """Подготовка перед каждым тестом"""
        self.driver = webdriver.Chrome()  # Или другой браузер
        
        # Создаём объекты страниц
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def tearDown(self):
        """Завершение после каждого теста"""
        self.driver.quit()

    def test_purchase_flow(self):
        """Тест: покупка товаров с проверкой итоговой суммы"""
        
        # 1. Открыть сайт магазина
        self.login_page.open("https://www.saucedemo.com/")
        
        # 2. Авторизоваться как standard_user
        self.login_page.login("standard_user", "secret_sauce")
        
        # 3. Добавить товары в корзину
        self.inventory_page.add_backpack()
        self.inventory_page.add_tshirt()
        self.inventory_page.add_onesie()
        
        # 4. Перейти в корзину
        self.inventory_page.go_to_cart()
        
        # 5. Нажать Checkout
        self.cart_page.click_checkout()
        
        # 6. Заполнить форму данными
        self.checkout_page.fill_info(
            firstname="Иван",
            lastname="Иванов",
            zipcode="123456"
        )
        
        # 7. Получить итоговую стоимость
        total = self.checkout_page.get_total_price()
        
        # 8. Проверить, что итоговая сумма равна $58.29
        expected_total = "$58.29"
        self.assertEqual(total, expected_total, f"Ожидаемая сумма: {expected_total}, фактическая: {total}")


if __name__ == "__main__":
    unittest.main()
