from selenium import webdriver
from calculator_page import CalculatorPage


def test_calculator_math_logic():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome()

    try:
        # Создаем объект страницы (Page Object)
        page = CalculatorPage(driver)

        # 1. Открыть страницу
        page.open()

        # 2. Ввести значение 45 в поле задержки
        page.set_delay(45)

        # 3. Нажать кнопки: 7, +, 8, =
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

        # 4. Проверить (assert), что результат 15
        # Ожидаем появления текста с учетом долгой задержки (50 секунд)
        page.wait_for_result("15", timeout=50)

        # Получаем фактический текст и проверяем его
        actual_text = page.get_screen_text()
        expected_text = "15"

        assert expected_text in actual_text, (
            f"Ожидался результат, '{expected_text}', но получено: '{actual_text}'"
            )
        print("Тест пройден успешно!")

    except Exception as e:
        print(f"Тест упал с ошибкой: {e}")
        raise e
    finally:
        # Закрываем браузер в любом случае
        driver.quit()


if __name__ == "__main__":
    test_calculator_math_logic()
