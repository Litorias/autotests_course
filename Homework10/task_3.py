# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize(
    "args, expected",
    [
        ((100, 5, 5), 4),
        ((100, 10, 2, 2), 2.5),
        ((100, -10, 2, 2), -2.5),
        pytest.param((100, 0, 2), pytest.raises(ZeroDivisionError), marks=pytest.mark.skip(reason="деление на ноль")),
        pytest.param((100, 5), 20, marks=pytest.mark.smoke),
    ]
)
def test_all_division(args, expected):
    if isinstance(expected, type):
        with expected:
            all_division(*args)
    else:
        assert all_division(*args) == expected
