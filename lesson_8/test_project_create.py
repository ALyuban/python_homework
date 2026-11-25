import os
import pytest
import requests
from dotenv import load_dotenv

# 1. Загружаем переменные из файла .env в окружение системы
load_dotenv()

# 2. Читаем переменные из окружения
# Если переменная не найдена, вернется None
BASE_URL = os.getenv("YOUGILE_BASE_URL")
API_TOKEN = os.getenv("YOUGILE_API_TOKEN")
REAL_USER_ID = os.getenv("REAL_USER_ID")

# Проверка: если токен не загрузился, сразу прерываем выполнение
if not API_TOKEN:
    raise ValueError("КРИТИЧЕСКАЯ ОШИБКА: YOUGILE_API_TOKEN не найден в .env файле!")

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

class TestCreateProject:

    def test_create_project_positive(self):
        """Позитивный тест: создание проекта"""
        url = f"{BASE_URL}/api-v2/projects"

        payload = {
            "title": "Secure Test Project",
            "users": {
                REAL_USER_ID: "admin"
            }
        }

        response = requests.post(url, json=payload, headers=HEADERS)

        assert response.status_code in [200, 201], \
            f"Ошибка! Статус: {response.status_code}, Ответ: {response.text}"

        assert "id" in response.json()
        print(f"\n✅ Проект создан. ID: {response.json()['id']}")

    def test_create_project_negative_no_title(self):
        """Негативный тест: без названия"""
        url = f"{BASE_URL}/api-v2/projects"
        payload = {"users": {REAL_USER_ID: "admin"}}

        response = requests.post(url, json=payload, headers=HEADERS)
        assert response.status_code == 400

if __name__ == "__main__":
    tester = TestCreateProject()
    tester.test_create_project_positive()
