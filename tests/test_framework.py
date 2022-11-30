import pytest

from main.framework import count_unical_symbol, count_unical_symbol_in_list, NotStringOrList


@pytest.mark.parametrize("str_,expected", [
    ('a', 1),
    ('abc', 3),
    ('', 0),
    ('abcdab', 2),
    ])
def test_string_positive(str_, expected):
    assert count_unical_symbol('a') == 1


@pytest.mark.parametrize('_list, expected', [
    (['a', 'bc'], [1, 2]),
    (['aaaab', 'bcbcbcbc'], [1, 0]),
    (['abcde', '7123aaa3215'], [5, 2]),
    (('qwerty', 'qweqwe'), [6, 0]),
    (('qwewe', '123'), [1, 3]),
    ({'hello'}, [3]),
    ])
def test_list_positive(_list, expected):
    assert count_unical_symbol_in_list(_list) == expected


def test_exception_string():
    with pytest.raises(NotStringOrList) as error:
        count_unical_symbol(123)
    assert 'You must use string type' == str(error.value)


def test_exception_list():
    with pytest.raises(NotStringOrList) as error:
        count_unical_symbol_in_list(123)
    assert 'You must use list, tuple or set type' == str(error.value)
