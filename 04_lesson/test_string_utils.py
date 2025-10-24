import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),     # Один пробел
    (" 123", "123"),           # Числа как строка
    ("   python", "python"),   # Несколько пробелов
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),            # Пустая строка
    ("   ", ""),         # Только пробелы
    ("  !@#", "!@#")     # Спец символы с пробелами
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),       # Символ в начале
    ("SkyPro", "P", True),       # Символ в середине
    ("SkyPro", "o", True),       # Символ в конце
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [

 ("SkyPro", "U", False),  # Нет такого символа
 ("python", "f", False),  # Нет такого символа
 ("12345", "6", False),  # Нет такой цифры
])
def test_contains_negative(string, symbol, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected:
            string_utils.contains(string, symbol)
    else:
        assert string_utils.contains(string, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),  # Удаление одного символа
    ("SkyPro", "Pro", "Sky"),  # Удаление подстроки
    ("123456", "3", "12456"),  # Удаление цифры
])
def test_delete_symbol_positive(input_string, symbol, expected):
    assert string_utils.delete_symbol(input_string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_string, symbol, expected", [
    ("a", "b", "a"),          # Символа нет в строке
    ("text", "", "text"),     # Пустой символ
    ("", "a", ""),            # Пустая строка
])
def test_delete_symbol_negative(input_string, symbol, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected:
            string_utils.delete_symbol(input_string, symbol)
    else:
        assert string_utils.delete_symbol(input_string, symbol) == expected
