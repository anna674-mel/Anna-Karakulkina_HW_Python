import unittest
from selenium import webdriver
from FormCalculatorPage import CalculatorPage  # Импорт класса страницы


class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        """Подготовка перед каждым тестом"""
        self.driver = webdriver.Chrome()  # Или другой браузер
        self.calculator = CalculatorPage(self.driver)

    def tearDown(self):
        """Завершение после каждого теста"""
        self.driver.quit()

    def test_calculator_operation(self):
        """Тест: вычисление 7 + 8 с задержкой 45 сек"""
        # Открыть страницу калькулятора
        self.calculator.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        # Установить задержку 45 секунд
        self.calculator.set_delay(45)
        
        # Нажать кнопки: 7 → + → 8 → =
        self.calculator.click_number_7()
        self.calculator.click_plus()
        self.calculator.click_number_8()
        self.calculator.click_equals()
        
        # Проверить результат через 45+ секунд
        result = self.calculator.get_result()
        self.assertEqual(result, "15", f"Ожидаемый результат: 15, фактический: {result}")


if __name__ == "__main__":
    unittest.main()
