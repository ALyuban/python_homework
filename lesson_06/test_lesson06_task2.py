from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_session_storage_auth():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # Ваши данные куки
    user1_cookies = [
        {'name': 'SESSION', 'value': 'YmViY2RmYzgtZGRmMy00MWRlLTg2NzgtNzBhNTk4Y2I3NmZm'}
    ]

    user2_cookies = [
        {'name': 'SESSION', 'value': 'OTYxODljMWUtMjg2Mi00NjRiLTg4ZjMtYTIzMjUwYTM2NWFl'}
    ]

    # Ваши ссылки на профили
    url_user1_profile = "https://gitflic.ru/user/ldima"
    url_user2_profile = "https://gitflic.ru/user/lanna"

    try:
        # --- ПРОВЕРКА ПОЛЬЗОВАТЕЛЯ 1 ---
        print("Авторизация Пользователя 1...")
        # 1. Сначала заходим на домен, чтобы Selenium знал, к какому сайту привязать куки
        driver.get("https://gitflic.ru/")

        # 2. Добавляем куки
        for cookie in user1_cookies:
            driver.add_cookie(cookie)

        # 3. Обновляем, чтобы сессия применилась
        driver.refresh()

        # 4. Переходим в профиль
        driver.get(url_user1_profile)

        # 5. Запоминаем текущий URL (чтобы убедиться, что мы не вылетели на страницу логина)
        url1 = driver.current_url
        print(f"Текущий URL (Пользователь 1): {url1}")

        # --- ПЕРЕКЛЮЧЕНИЕ НА ПОЛЬЗОВАТЕЛЯ 2 ---
        print("\nОчистка данных и переход к Пользователю 2...")
        driver.delete_all_cookies()  # Удаляем сессию первого пользователя

        # 6. Заходим на домен (снова, для чистоты контекста)
        driver.get("https://gitflic.ru/")

        # 7. Добавляем куки второго пользователя
        for cookie in user2_cookies:
            driver.add_cookie(cookie)

        # 8. Обновляем и переходим в профиль
        driver.refresh()
        driver.get(url_user2_profile)

        # 9. Запоминаем текущий URL
        url2 = driver.current_url
        print(f"Текущий URL (Пользователь 2): {url2}")

        # --- ПРОВЕРКА РЕЗУЛЬТАТА ---
        # Если куки сработали, URL не должен быть страницей входа/логина
        # И URL первого и второго пользователя должны отличаться
        assert url1 != url2, "Ошибка: URL пользователей совпали!"
        assert "login" not in url1.lower(), "Ошибка: Пользователь 1 не авторизован (перенаправлен на login)"
        assert "login" not in url2.lower(), "Ошибка: Пользователь 2 не авторизован (перенаправлен на login)"

        print("\n✅ Тест пройден успешно!")
        print(f"Подтверждено: Пользователь 1 зашел как {url1}, а Пользователь 2 как {url2}")

    except Exception as e:
        print(f"\n❌ Произошла ошибка во время теста: {e}")

    finally:
        # Закрываем браузер в любом случае
        driver.quit()

if __name__ == "__main__":
    test_session_storage_auth()