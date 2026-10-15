import pytest
from string_utils import StringUtils

class TestStringUtils:

    @pytest.fixture
    def utils(self):
        """Фикстура для создания экземпляра класса перед каждым тестом."""
        return StringUtils()

    # --- Тесты для capitalize ---
    @pytest.mark.parametrize("input_str, expected", [
        ("skypro", "Skypro"),      # Обычная строка
        ("SKYPRO", "Skypro"),      # Все заглавные
        ("sKyPrO", "Skypro"),      # Смешанный регистр
        ("", ""),                  # Пустая строка (граница)
        ("123", "123"),            # Числа в строке
    ])
    def test_capitalize_positive(self, utils, input_str, expected):
        assert utils.capitalize(input_str) == expected

    def test_capitalize_negative(self, utils):
        with pytest.raises(AttributeError):
            utils.capitalize(123)  # Передача числа вместо строки

    # --- Тесты для trim ---
    @pytest.mark.parametrize("input_str, expected", [
        ("   skypro", "skypro"),   # Пробелы в начале
        ("skypro   ", "skypro   "), # Пробелы в конце (не должны удаляться по ТЗ)
        ("   skypro   ", "skypro   "), # Пробелы и в начале, и в конце
        ("skypro", "skypro"),      # Без пробелов
        ("   ", ""),               # Только пробелы
        ("", ""),                  # Пустая строка
    ])
    def test_trim_positive(self, utils, input_str, expected):
        assert utils.trim(input_str) == expected

    def test_trim_negative(self, utils):
        with pytest.raises(AttributeError):
            utils.trim(None)

    # --- Тесты для contains ---
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),     # Символ в начале
        ("SkyPro", "o", True),     # Символ в середине/конце
        ("SkyPro", "U", False),    # Символа нет
        ("SkyPro", "Sky", True),   # Поиск подстроки (работает как символ)
        ("", "S", False),          # Пустая строка
        ("SkyPro", "", True),      # Поиск пустой строки (в Python "" в строке - это True)
    ])
    def test_contains_positive(self, utils, string, symbol, expected):
        assert utils.contains(string, symbol) == expected

    @pytest.mark.parametrize("string, symbol", [
        (123, "1"),                # Строка — число
        ("SkyPro", 1),             # Символ — число
        (None, "S"),               # Строка — None
    ])
    def test_contains_negative(self, utils, string, symbol):
        with pytest.raises((TypeError, AttributeError)):
            utils.contains(string, symbol)

    # --- Тесты для delete_symbol ---
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "k", "SyPro"),     # Удаление одного символа
        ("SkyPro", "Pro", "Sky"),     # Удаление подстроки
        ("aaaaa", "a", ""),           # Удаление всех одинаковых символов
        ("SkyPro", "Z", "SkyPro"),    # Символа нет (строка не меняется)
        ("", "a", ""),                # Пустая строка
        ("abc", "", "abc"),           # Удаление пустой строки (не должно ничего менять)
    ])
    def test_delete_symbol_positive(self, utils, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected

    def test_delete_symbol_negative(self, utils):
        with pytest.raises((TypeError, AttributeError)):
            utils.delete_symbol(None, "a")