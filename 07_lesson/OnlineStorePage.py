from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        username_field = self.wait.until(EC.presence_of_element_located(self.username_input))
        username_field.send_keys(username)
        
        password_field = self.wait.until(EC.presence_of_element_located(self.password_input))
        password_field.send_keys(password)
        
        login_btn = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_btn.click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Локаторы товаров
        self.backpack_add = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt_add = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cartlink = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.backpack_add))
        btn.click()

    def add_tshirt(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.tshirt_add))
        btn.click()

    def add_onesie(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.onesie_add))
        btn.click()

    def go_to_cart(self):
        cart_btn = self.wait.until(EC.element_to_be_clickable(self.cartlink))
        cart_btn.click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.checkoutbutton = (By.ID, "checkout")

    def click_checkout(self):
        checkout_btn = self.wait.until(EC.element_to_be_clickable(self.checkoutbutton))
        checkout_btn.click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        
        self.firstnameinput = (By.ID, "first-name")
        self.lastnameinput = (By.ID, "last-name")
        self.zipcodeinput = (By.ID, "postal-code")
        self.continuewbutton = (By.ID, "continue")
        self.totalprice = (By.CLASS_NAME, "summary_total_label")

    def fill_info(self, firstname, lastname, zipcode):
        first_name_field = self.wait.until(EC.presence_of_element_located(self.firstnameinput))
        first_name_field.send_keys(firstname)
        
        last_name_field = self.wait.until(EC.presence_of_element_located(self.lastnameinput))
        last_name_field.send_keys(lastname)
        
        zip_code_field = self.wait.until(EC.presence_of_element_located(self.zipcodeinput))
        zip_code_field.send_keys(zipcode)
        
        continue_btn = self.wait.until(EC.element_to_be_clickable(self.continuewbutton))
        continue_btn.click()

    def get_total_price(self):
        total_element = self.wait.until(EC.visibility_of_element_located(self.totalprice))
        return total_element.text
