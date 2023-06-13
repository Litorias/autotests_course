# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного.
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты.

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


def test_all_division_positive():
    assert all_division(100, 5, 5) == 4


def test_all_division_positive2():
    assert all_division(100, 10, 2, 2) == 2.5


def test_all_division_negative():
    assert all_division(100, -10, 2, 2) == -2.5


# smoke маркер
@pytest.mark.smoke
def test_all_division_smoke():
    assert all_division(100, 5) == 20


# тест деления на ноль
def test_all_division_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(100, 0, 2)
