from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://www.saucedemo.com/"
        # Локаторы
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        """Открывает главную страницу авторизации."""
        self.driver.get(self.url)

    def login(self, username, password):
        """Вводит логин, пароль и нажимает кнопку входа."""
        self.wait.until(
            EC.presence_of_element_located(
                self.username_field)).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Локаторы кнопок добавления товаров
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, item_type):
        """Добавляет товар в корзину по его типу."""
        if item_type == "backpack":
            self.driver.find_element(*self.add_backpack).click()
        elif item_type == "tshirt":
            self.driver.find_element(*self.add_tshirt).click()
        elif item_type == "onesie":
            self.driver.find_element(*self.add_onesie).click()

    def go_to_cart(self):
        """Переходит на страницу корзины."""
        self.wait.until(EC.element_to_be_clickable(self.cart_link)).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self):
        """Нажимает кнопку оформления заказа (Checkout)."""
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Локаторы полей формы оформления заказа
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        # Локатор итоговой стоимости
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, fname, lname, zip_code):
        self.wait.until(
            EC.visibility_of_element_located(self.first_name)).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_text(self):
        """Возвращает текст итоговой стоимости со страницы."""
        element = self.wait.until(EC.visibility_of_element_located(
            self.total_label))
        return element.text
