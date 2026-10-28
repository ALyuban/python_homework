from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # Сохраняем текущий URL
    initial_url = driver.current_url

    # Создаем объект ожидания (ждем максимум 10 секунд)
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Находим поле custname и ждем, пока оно станет доступным для ввода
        name_field = wait.until(EC.element_to_be_clickable((By.NAME, "custname")))
        name_field.send_keys("Ivan")

        # 2. Находим кнопку Submit. 
        # Используем более гибкий XPath: 
        # Ищем либо input с типом submit, либо кнопку, в тексте которой ЕСТЬ слово 'Submit'
        submit_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='submit'] | //button[contains(text(), 'Submit')] | //input[contains(@value, 'Submit')]")
        ))
        submit_button.click()

        # 3. Ждем, пока URL изменится (ждем, пока новый URL не станет отличаться от старого)
        wait.until(lambda d: d.current_url != initial_url)

        new_url = driver.current_url
        print(f"Тест пройден! Новый URL: {new_url}")
        assert new_url != initial_url

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        # Делаем скриншот для отладки, если что-то пошло не так
        driver.save_screenshot("error_screenshot.png")
        raise e
    finally:
        driver.quit()

if __name__ == "__main__":


    test_form_submission()