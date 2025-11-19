from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        # Локаторы элементов
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_screen = (By.CSS_SELECTOR, ".screen")
        self.spinner = (By.CSS_SELECTOR, "#spinner")

    def open(self, url):
        """Открыть страницу калькулятора"""
        self.driver.get(url)

    def set_delay(self, value):
        """Установить значение задержки"""
        element = self.wait.until(EC.presence_of_element_located(self.delay_input))
        element.clear()
        element.send_keys(str(value))

    def click_number_7(self):
        """Нажать кнопку 7"""
        button = self.wait.until(EC.element_to_be_clickable(self.button_7))
        button.click()

    def click_plus(self):
        """Нажать кнопку +"""
        button = self.wait.until(EC.element_to_be_clickable(self.button_plus))
        button.click()

    def click_number_8(self):
        """Нажать кнопку 8"""
        button = self.wait.until(EC.element_to_be_clickable(self.button_8))
        button.click()

    def click_equals(self):
        """Нажать кнопку ="""
        button = self.wait.until(EC.element_to_be_clickable(self.button_equals))
        button.click()

    def get_result(self):
        """Получить текущий результат из экрана"""
        element = self.wait.until(EC.visibility_of_element_located(self.result_screen))
        return element.text
    
    def invisible_element(self):
        self.wait.until(EC.invisibility_of_element_located(self.spinner))
    
    def visible_element(self):
        self.wait.until(EC.visibility_of_element_located(self.spinner))
