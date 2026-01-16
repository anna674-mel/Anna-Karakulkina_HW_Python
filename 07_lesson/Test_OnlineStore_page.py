from selenium import webdriver
# Импортируем классы страниц (если они в отдельных файлах)
from OnlineStorePage import LoginPage
from OnlineStorePage import InventoryPage
from OnlineStorePage import CartPage
from OnlineStorePage import CheckoutPage


def test_online_store_operation():
    # Создаём объект опций Firefox
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Открыть сайт магазина
    login_page.open("https://www.saucedemo.com/")
    # 2. Авторизоваться как standard_user
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавить товары в корзину
    inventory_page.add_backpack()
    inventory_page.add_tshirt()
    inventory_page.add_onesie()

    # 4. Перейти в корзину
    inventory_page.go_to_cart()

    # 5. Нажать Checkout
    cart_page.click_checkout()

    # 6. Заполнить форму данными
    checkout_page.fill_info(
        firstname="Иван",
        lastname="Иванов",
        zipcode="123456"
    )

    # 7. Получить итоговую стоимость
    total = checkout_page.get_total_price()
        
    # 8. Проверить, что итоговая сумма равна $58.29
    expected_total = "Total: $58.29"
    assert total == expected_total, (f"Ожидаемая сумма: {expected_total}, фактическая: {total}")

    driver.quit()
