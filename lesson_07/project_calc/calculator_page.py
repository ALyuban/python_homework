from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        # Локаторы
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._screen = (By.CLASS_NAME, "screen")

    def open(self):
        """Открывает страницу калькулятора."""
        self.driver.get(self.url)

    def set_delay(self, seconds):
        """Очищает поле задержки и вводит значение."""
        element = self.wait.until(
            EC.presence_of_element_located(self._delay_input))
        element.clear()
        element.send_keys(str(seconds))

    def click_button(self, text):
        """Находит кнопку по тексту внутри span и кликает."""
        # Используем XPATH, как в вашем исходном коде
        xpath = f"//span[normalize-space()='{text}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def wait_for_result(self, expected_text, timeout=50):
        """Ждет, пока в поле результата появится нужный текст."""
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._screen, expected_text),
            f"Результат '{expected_text}' не появился в поле .screen вовремя"
        )

    def get_screen_text(self):
        """Возвращает текущий текст из поля вывода."""
        return self.driver.find_element(*self._screen).text
