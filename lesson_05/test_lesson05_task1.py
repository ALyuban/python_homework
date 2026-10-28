from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_navigation():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        base_url = "https://httpbin.qa-territory.online"
        driver.get(base_url)
        print(f"Открыта страница: {driver.current_url}")


        form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
        form_link.click()

        assert "/forms/post" in driver.current_url, f"Ошибка: URL не изменился. Текущий: {driver.current_url}"
        print("✅ Шаг 3 пройден: URL изменился на /forms/post")

        driver.back()

        assert driver.current_url == base_url, f"Ошибка: Не удалось вернуться на главную. Текущий: {driver.current_url}"
        print("✅ Шаг 5 пройден: Вернулись на исходную страницу")

        print("\n🎉  ТЕСТ 1 ЗАВЕРШЕН УСПЕШНО!")

    except AssertionError as e:
        print(f"\n❌ ТЕСТ ПРОВАЛЕН (AssertionError): {e}")
    except Exception as e:
        print(f"\n❌ ПРОИЗОШЛА ОШИБКА: {e}")
    finally:
        # Закрытие браузера в любом случае
        driver.quit()

if __name__ == "__main__":

    
    test_navigation()