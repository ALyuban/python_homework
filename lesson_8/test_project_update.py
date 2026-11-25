import os
import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("YOUGILE_BASE_URL")
API_TOKEN = os.getenv("YOUGILE_API_TOKEN")
PROJECT_ID = "02c79075-b12c-475e-9b5a-63c26052984c"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

class TestUpdateProject:

    def test_update_project_title_positive(self):
        print("\nзапуск позитивного теста")
        url_put = f"{BASE_URL}/api-v2/projects/{PROJECT_ID}"
        url_get = f"{BASE_URL}/api-v2/projects/{PROJECT_ID}" # URL для проверки
        new_title = "Success Title"
        payload = {"title": new_title}

        # 1. Отправляем запрос на обновление
        response_put = requests.put(url_put, json=payload, headers=HEADERS)
        assert response_put.status_code == 200, f"Ошибка PUT: {response_put.text}"

        # 2. Делаем GET запрос, чтобы убедиться, что данные реально сохранились
        response_get = requests.get(url_get, headers=HEADERS)
        assert response_get.status_code == 200, f"Ошибка GET: {response_get.text}"

        actual_title = response_get.json().get("title")

        # Проверяем, что название совпадает
        assert actual_title == new_title, f"Ожидали '{new_title}', но получили '{actual_title}'"

        print("тест пройден успешно")

    def test_update_project_invalid_id_negative(self):
        print("\nзапуск негативного теста")
        invalid_id = "invalid-id-123"
        url = f"{BASE_URL}/api-v2/projects/{invalid_id}"
        payload = {"title": "Fail"}

        response = requests.put(url, json=payload, headers=HEADERS)

        assert response.status_code in [400, 404]
        print("тест пройден (неверный ID)")

    def test_update_project_empty_title_negative(self):
        print("\nзапуск негативного теста")
        url = f"{BASE_URL}/api-v2/projects/{PROJECT_ID}"
        payload = {"title": ""}

        response = requests.put(url, json=payload, headers=HEADERS)

        assert response.status_code == 400
        print("тест пройден (пустое название)")