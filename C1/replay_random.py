# import random
# rand_set = set()
# i = 0
# while True:
#     num = random.randint(1, 10)
#     if num in rand_set:
#         break
#     rand_set.add(num)
# print('The replay occurred on {} iteration.'.format(len(rand_set) + 1))
# import re
#
# s = '@something.com'
# try:
#     extension = s.rsplit(sep='.', maxsplit=1)
#     web_name = extension[0].rsplit(sep='@', maxsplit=1)[1]
#     user_name = s.rsplit(sep='@', maxsplit=1)[0]
#     extension = extension[1]
#     print(len(user_name),  extension, web_name)
#     if web_name.isalnum() and extension.isalpha() and (len(extension) <= 3) and len(user_name) > 1
#     and bool(re.match("^[A-Za-z0-9_-]*$", user_name)):
#         print('True')
#     else:
#         print('False')
#
# except:
#     print('False')

# TODO Сдвиг массива
# a = list(range(1, 11))
# d = 5
# print(a)
# # for _ in range(d):
# a_before = list(a[:d])
# a_after = list(a[d:])
# new_a = a_after + a_before
# print(new_a, sep='')

# TODO декоратор (чтобы результат summatora() записывался в fail) - понял
# def logger(filename):
#     def decorator(func):
#         def inner(*args, **kwargs):
#             resault = func(*args, **kwargs)
#             with open(filename, 'w') as f:
#                 f.write(str(resault))
#             return resault
#         return inner
#     return decorator
#
#
# @logger("new_text.txt")
# def summator(num_list):
#     return sum(num_list)
#
#
# print('Resault in summator(inner) - {}'.format(summator([1, 2, 3, 4, 5, 15])))
# with open('new_text.txt', 'r') as f:
#     print(f.read())

# TODO 2 Декоратора - понял
# def first_decoration(func):
#     def inner():
#         print("This is inner in first_decoration!")
#         func()
#         print('11111')
#     return inner
#
#
# def second_decoration(func):
#     def inner():
#         print('This is inner in second_decoration!)')
#         func()
#         print('2222222')
#     return inner
#
#
# @second_decoration
# @first_decoration
# def greeting():
#     print('Hello, my lord')
#
#
# greeting()

# TODO Разбираемся - понял
# def bread(func):
#     def inner():
#         print("<______>")
#         func()
#         print('<_____>')
#
#     return inner
#
#
# def vegetables(func):
#     def inner():
#         print('--Tamato--')
#         func()
#         print('--Морковка--')
#
#     return inner
#
#
# @bread
# @vegetables
# def sandwich(food="-колбаска--"):
#     print(food)
#
#
# sandwich()