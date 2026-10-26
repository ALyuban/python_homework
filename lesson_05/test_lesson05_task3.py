from selenium import webdriver
from selenium.webdriver.common.by import By  


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")

    link_count = len(links)
    print(f"Найдено ссылок: {link_count}")
    assert link_count == 9, f"Ошибка: Ожидалось 9 ссылок, но найдено {link_count}"

    for index, link in enumerate(links):
        assert link.is_displayed(), f"Ошибка: Ссылка под номером {index} не отображается на странице"
    print("Все ссылки успешно отображаются.")

    first_link_text = links[0].text
    print(f"Текст первой ссылки: '{first_link_text}'")
    assert "1" in first_link_text, f"Ошибка: Текст первой ссылки '{first_link_text}' не содержит '1'"

    print("Все проверки пройдены успешно!")
    driver.quit()

if __name__ == "__main__":


    test_multiple_elements()