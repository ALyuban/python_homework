from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, timeout=10)

    # 1. Откройте страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. Очистить поле и ввести 45
    input_delay = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    input_delay.clear()
    input_delay.send_keys("45")

    # 3. Нажмите на кнопки
    driver.find_element(By.XPATH, "//span[normalize-space()='7']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='+']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='8']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='=']").click()

    # 4. Проверьте (assert), что в окне отобразится результат 15
    WebDriverWait(driver, timeout=50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"),
        "Результат '15' не появился в поле .screen вовремя"
    )

    actual_text = driver.find_element(
        By.CLASS_NAME, "screen").text
    assert "15" in actual_text, f"Ожидался результат 15, но получили {
        actual_text}"

    driver.quit()


if __name__ == "__main__":
    test_calculator()
