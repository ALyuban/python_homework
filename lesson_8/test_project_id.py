import pytest
import requests

# Константы из вашего задания
BASE_URL = "https://ru.yougile.com"
API_TOKEN = "ESGcIgdZlE4iBz3Fui9pW-cCt0jUKwpadN8PqYuY-ndl9tTdMfCxQWcEmWJObB1u"
PROJECT_ID = "d631e485-0c8f-4bf9-a4d4-3a50f6d20165"

# Общие заголовки для всех запросов
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

class TestGetProjectByID:

    def test_get_project_by_id_positive(self):
        """
        Позитивный тест: получение существующего проекта по ID.
        """
        print("\nзапуск позитивного теста")
        url = f"{BASE_URL}/api-v2/projects/{PROJECT_ID}"

        response = requests.get(url, headers=HEADERS)

        # Проверка статус-кода
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}. Ответ: {response.text}"

        data = response.json()

        # Проверка структуры ответа
        assert "id" in data, "В ответе отсутствует поле 'id'"
        assert "title" in data, "В ответе отсутствует поле 'title'"
        assert data["id"] == PROJECT_ID, f"ID в ответе ({data['id']}) не совпадает с запрошенным ({PROJECT_ID})"

        print("тест пройден успешно")

    def test_get_project_by_id_negative(self):
        """
        Негативный тест: попытка получить проект по несуществующему ID.
        """
        print("\nзапуск негативного теста")
        invalid_id = "00000000-0000-0000-0000-000000000000"
        url = f"{BASE_URL}/api-v2/projects/{invalid_id}"

        response = requests.get(url, headers=HEADERS)

        # Проверка статус-кода 404
        assert response.status_code == 404, f"Ожидался 404 для неверного ID, получен {response.status_code}"

        print("тест пройден (негативный тест: получение неверного ID)")