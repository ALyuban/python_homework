from selenium import webdriver
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage


def test_sauce_demo_purchase():
    # Инициализация Firefox
    driver = webdriver.Firefox()

    try:
        # 1. Создаем объекты страниц
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # 2. Открыть сайт и авторизоваться
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # 3. Добавить товары в корзину
        inventory_page.add_to_cart("backpack")
        inventory_page.add_to_cart("tshirt")
        inventory_page.add_to_cart("onesie")

        # 4. Перейти в корзину
        inventory_page.go_to_cart()

        # 5. Нажать Checkout
        cart_page.click_checkout()

        # 6. Заполнить форму
        checkout_page.fill_form("Anna", "Lyuban", "440068")

        # 7. Получить итоговую стоимость
        actual_total = checkout_page.get_total_text()
        expected_total = "Total: $58.29"

        # 8. ПРОВЕРКА (Assert)
        assert actual_total == expected_total, (
            f"Ошибка! Ожидалось '{expected_total}', но фактически получено: '{actual_total}'"
        )
        print("Тест пройден успешно!")

    except Exception as e:
        print(f"Тест упал с ошибкой: {e}")
        raise e
    finally:
        # 9. Закрыть браузер
        driver.quit()


if __name__ == "__main__":
    test_sauce_demo_purchase()
