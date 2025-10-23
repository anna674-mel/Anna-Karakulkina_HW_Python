import pytest
from string_utils import StringUtils


string_utils = StringUtils()


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
