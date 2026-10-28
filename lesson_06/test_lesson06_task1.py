from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading():
    driver = webdriver.Chrome()
    # Создаем объект для явных ожиданий (максимум 10 секунд)
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Откройте страницу
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # 2. Найдите и нажмите на кнопку "Start" (используя CSS-селектор)
        start_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button")))
        start_button.click()

        # 3. Дождитесь появления текста "Hello World!"
        # Текст появляется внутри элемента с id="finish"
        finish_element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))

        # 4. Сделайте скриншот страницы
        driver.save_screenshot("screenshot.png")

        # 5. Проверьте, что появившийся текст равен "Hello World!"
        assert finish_element.text == "Hello World!"
        print("Тест пройден успешно: текст 'Hello World!' найден.")

    except Exception as e:
        print(f"Тест провален: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_dynamic_loading()