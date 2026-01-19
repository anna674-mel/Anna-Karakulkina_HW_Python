from selenium import webdriver
from FormCalculatorPage import CalculatorPage


def test_calculator_operation():
    driver = webdriver.Chrome()
    calculator = CalculatorPage(driver)

    calculator.open(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    # Установить задержку 45 секунд
    calculator.set_delay(45)

    calculator.click_number_7()
    calculator.click_plus()
    calculator.click_number_8()
    calculator.click_equals()
    calculator.visible_element()
    calculator.invisible_element()

    # Проверить результат через 45+ секунд
    result = calculator.get_result()
    assert result == "15", (
        f"Результат не совпадает с ожидаемым. Получено: {result}"
    )

    driver.quit()
