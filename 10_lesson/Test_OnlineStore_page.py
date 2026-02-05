from selenium import webdriver
from OnlineStorePage import LoginPage
from OnlineStorePage import InventoryPage
from OnlineStorePage import CartPage
from OnlineStorePage import CheckoutPage
import allure


@allure.title("Тестирование онлайн магазина")
@allure.description("Тест проверяет итоговую сумму стоимости товаров")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_online_store_operation():
    # Создаём объект опций Firefox
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    """
        Открывает сайт магазина
    """
    login_page.open("https://www.saucedemo.com/")
    """
        Авторизация
    """
    login_page.login("standard_user", "secret_sauce")
    """
        Добавляет товары в корзину
    """
    inventory_page.add_backpack()
    inventory_page.add_tshirt()
    inventory_page.add_onesie() 
    """
        Переход в корзину
    """
    inventory_page.go_to_cart()
    """
       Нажатие кнопки Checkout
    """

    cart_page.click_checkout()

    """
        Заполнение формы данными
    """
    checkout_page.fill_info(
        firstname="Иван",
        lastname="Иванов",
        zipcode="123456"
    )

    """
        Получение итоговой стоимости
    """
    total = checkout_page.get_total_price()
    """
        Проверка итоговой суммы
    """
    expected_total = "Total: $58.29"
    assert total == expected_total, (f"Ожидаемая сумма: {expected_total}, фактическая: {total}")

    driver.quit()
