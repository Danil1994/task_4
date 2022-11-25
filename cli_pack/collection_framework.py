from collections import Counter
from functools import wraps
from typing import Iterable

Save_results = {}


class NotStringOrList(TypeError):
    pass


def save_result(func):
    @wraps(func)
    def wrapper(string):
        if result := Save_results.get(string):
            return result
        else:
            result = func(string)
            Save_results[string] = result
            return result

    return wrapper


@save_result
def count_unical_symbol(string: str) -> int:
    if not isinstance(string, str):
        raise NotStringOrList('You must use string type')

    counting_object = Counter(string)
    unical_symbol = [symbol for symbol in counting_object if counting_object[symbol] == 1]
    Save_results[string] = len(unical_symbol)
    return len(unical_symbol)


def count_unical_symbol_in_list(list_object: Iterable) -> list:
    if not isinstance(list_object, Iterable):
        raise NotStringOrList('You must use list, tuple or set type')

    answer = list(map(count_unical_symbol, list_object))
    return answer
