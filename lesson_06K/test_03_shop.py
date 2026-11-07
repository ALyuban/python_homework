from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    # Используем Chrome или Firefox (убедитесь, что драйвер установлен)
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    # 1. Откройте страницу: https://www.saucedemo.com/
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизуйтесь как пользователь standard_user.
    user_name = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']")))
    user_name.send_keys("standard_user")

    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("secret_sauce")

    login_btn = driver.find_element(By.XPATH, "//input[@id='login-button']")
    login_btn.click()

    # 3. Добавьте в корзину товары:
    wait.until(
        EC.presence_of_element_located(
            (By.ID, "inventory_container")))

    driver.find_element(
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element(
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
        ).click()
    driver.find_element(
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()

    # 4. Перейдите в корзину.
    basket_btn = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    basket_btn.click()

    # 5. Нажмите Checkout.
    checkout_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    # 6. Заполните форму своими данными.
    first_name = wait.until(
        EC.visibility_of_element_located((By.ID, "first-name")))
    first_name.send_keys("Анна")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Любан")

    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("440068")

    # 7. Нажмите кнопку Continue.
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    # 8. Прочитайте со страницы итоговую стоимость (Total).
    total_element = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text

    # 9. Закройте браузер.
    driver.quit()

    # 10. Проверьте, что итоговая сумма равна $58.29.
    assert total_text == "Total: $58.29", (
        f"Ожидалось 'Total: $58.29', но получено: {total_text}"
    )


if __name__ == "__main__":
    test_shop()
