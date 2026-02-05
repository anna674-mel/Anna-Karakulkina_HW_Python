from selenium import webdriver
from FormCalculatorPage import CalculatorPage
import allure


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работу калькулятора ")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_operation():
    driver = webdriver.Chrome()
    calculator = CalculatorPage(driver)
    """
        Открывает страницу калькулятора
    """
    calculator.open(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    """
        Тест устанавливает задержку калькулятора на 45 сек
    """
    calculator.set_delay(45)

    calculator.click_number_7()
    calculator.click_plus()
    calculator.click_number_8()
    calculator.click_equals()
    calculator.visible_element()
    calculator.invisible_element()

    """
    Тест проверяет работу калькулятора через 45+ секунд
    """
    result = calculator.get_result()
    assert result == "15", (
        f"Результат не совпадает с ожидаемым. Получено: {result}"
    )

    driver.quit()
