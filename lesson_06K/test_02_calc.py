from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, timeout=10)

    # 1. Откройте страницу https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в Google Chrome
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. В поле delay по умолчанию Leave значение 45
    input_delay = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    input_delay.send_keys("45")

    # 3. Нажмите на кнопки:
    submit_button_7 = driver.find_element(By.XPATH, "//span[normalize-space()='7']")
    submit_button_7.click()
    submit_button = driver.find_element(By.XPATH, "//span[normalize-space()='+']")
    submit_button.click()
    submit_button_8 = driver.find_element(By.XPATH, "//span[normalize-space()='8']")
    submit_button_8.click()
    submit_button = driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning']")
    submit_button.click()

    # 4. Проверьте (assert), что в окне отобразится результат через 15 секунд.
    window_field = WebDriverWait(driver, timeout=45).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='delay']")), "Результат через 15 секунд")
    driver.quit()