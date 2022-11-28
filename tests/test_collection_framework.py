import pytest

from collection_framework import count_unical_symbol, count_unical_symbol_in_list, NotStringOrList


@pytest.mark.parametrize('_str, expected', [
    ('a', 1),
    ('abc', 3),
    ('', 0),
    ('abcdab', 2),
    ])
def test_string_positive(_str, expected):
    assert count_unical_symbol(_str) == expected


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
