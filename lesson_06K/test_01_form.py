import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def driver():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()


def test_form_validation(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 15)

    # 1. Ждем загрузки страницы по первому элементу
    wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

    # 2. Заполнение формы
    def fill_field(name, text):
        field = wait.until(EC.presence_of_element_located((By.NAME, name)))
        field.clear()  # Очищаем поле перед вводом
        field.send_keys(text)

    fill_field("first-name", "Иван")
    fill_field("last-name", "Петров")
    fill_field("address", "Ленина, 55-3")
    fill_field("e-mail", "test@skypro.com")
    fill_field("phone", "+79858999878")

    # Тот самый проблемный Zip-code
    fill_field("zip-code", "")

    fill_field("city", "Москва")
    fill_field("country", "Россия")
    fill_field("job-position", "QA")
    fill_field("company", "SkyPro")

    # 3. Нажмите кнопку Submit
    submit_button = driver.find_element(
        By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    # 4. Проверяйте (assert): что поле Zip Code подсвечено красным.
    zip_code_field = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_code_field.get_attribute("class"), (
        "Поле Zip code должно быть красным!"
    )

    # 5. Проверяйте (assert): что остальные поля подсвечены зеленым.
    green_fields_ids = [
        "first-name", "last-name", "address", "city",
        "country", "e-mail", "phone", "job-position", "company"
    ]

    for field_id in green_fields_ids:
        field = driver.find_element(By.ID, field_id)
        field_classes = field.get_attribute("class")
        assert "alert-success" in field_classes, (
            f"Поле {field_id} должно быть зеленым! "
            f"Классы: {field_classes}"
        )
