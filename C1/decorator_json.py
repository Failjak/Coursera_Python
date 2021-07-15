import json
import functools


def to_json(func):
    @functools.wraps(func)
    def json_func(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return json_func


@to_json
def get_data():
    return {
        'data': 42
    }
get_data()  # вернёт '{"data": 42}'
#
#
# @to_json
# def f(a, b, c):
#     listing = []
#     listing.append(a)
#     listing.append(b)
#     listing.append(c)
#     return listing
#
#
# result = f(1, 2, 3)
# print(ascii(result))  # '[1, 2, 3]'
# print(type(result))  # <class 'str'>
# data = json.loads(result)
# print(data)  # [1, 2, 3]
# print(type(data))  # <class 'list'>
#

