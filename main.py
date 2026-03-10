# стуктуры данных и генераторы
# список (list, он же массив)
numbers = [1, 2, 3, 4, 5, 6, 7]
fruits = ['apple', 'orange', 'kiwi', 'orange']
mixed = [1, 'asd', 3.14, True]

letters = list('word')
print(letters)

letters.append('R')
print(letters)
letters.insert(1, 'new')
print(letters)
deleted = letters.pop(1)
print(deleted, letters)
letters.remove('r')
print(letters)

letters.sort() # мутирует
sorted(letters) # не мутирует
print(letters)

print(sorted(fruits, key=len))
letters.reverse()
print(letters)
print(len(letters), fruits.count('orange'), letters.index('d'))

# срезы (slice)
print(numbers[4])
print(numbers[2:4])
print(numbers[:6])
print(numbers[1:])
print(numbers[::2])
print(numbers[::-1])
numbers[0] = 'asd'
print(numbers)

# кортежи (tuple, неизменяемый массив)
# return a, b => (a, b)

empty = ()
print(type(empty))
numbers_t = (1, 2, 4)
mixed_t = (1, 3.14, True)

# {x:1, y:3}
point = 10, 20
print(point, type(point))
tup_1 = ('a',)
print(type(tup_1))
# numbers_t[0] = 10
# методы похожи на методы массивов (кроме мутирующих методов)

# операции со списками, кортежами
print([1, 2, 3] + ['a', 'b', 'c'])
print((1, 2, 3) + tuple('asd'))
print([0] * 10)
print(('a', ) * 4)
print(3 in [1, 2, 3])
print(3 in (1, 2, 4))
# деструктуризация списков и кортежей
price = [10, 56, 45, 67]
rub, *cop = price
print(cop)
price = (10, 56, 45, 67)
rub, *cop = price
print(rub)

# генераторы
# нужно создать массив из квадратов чисел от 1 до 10
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)

squares_2 = [i ** 2 for i in range(1, 11)]
print(squares_2)

# нужно создать массив из квадратов четных чисел от 1 до 10
squares = []
for i in range(1, 11):
    if (i % 2 == 0):
        squares.append(i ** 2)
print(squares)

squares_2 = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(squares_2)

# множества (set)
array = [2, 2, 2, 2]
tupl = (2, 3, 2, 3)
set_1 = set(array)
set_2 = set(tupl)
print(set_1, set_2)

# словари (dict, объекты)
dict_1 = {
    'key': 'value',
    'key2': 'value'
}

dict_2 = dict(name='Pavel', age=20)
print(dict_2)

# dict_3 = dict(("k1", "v1"))
dict_3 = dict([('key', 'val'), ('key2', 'val2')])
print(dict_3)

dict_4 = dict(zip(['k1', 'k2', 'k3'], ['v1', 'v2', 'v3']))
print(dict_4)
# ['k1', 'k2', 'k3']
# ['v1', 'v2', 'v3']
# zip() -> (k1, v1) (k2, v2) по индексам
# dict() -> {k1: v1, k2: v2}

# print(dict_4['k12'])

try:
    print(dict_4['k23'])
except:
    print('None')

print(dict_4.get('k34'))

print('k1' in dict_4)
print('k1' not in dict_4)

dict_4['k1'] = 123
print(dict_4)

del dict_4['k1']
print(dict_4)
print(dict_4.pop('k2', None))
# [1, 2, 3] -> [1, , 3]

dict_5 = dict(zip('asd', list(range(3))))
print(dict_5)

for key in dict_5:
    print(key, dict_5[key])

print(dict_5.items())
for key, value in dict_5.items():
    print(key, value)

print(dict_5.values())
print(dict_5.keys())

# №1 На вход дается строка. Необходимо вывести самое частое слово 
# в строке
# кружка стол кабинет Кружка
# str.split(' ')
# str.lower()
# str.upper()

# data = input().lower().split(' ')
# count_dict = dict()
# # переделать в генератор
# for item in data:
#     if item in count_dict:
#         count_dict[item] += 1
#     else:
#         count_dict[item] = 1

# count_dict = {word: data.count(word) for word in data}
# print(count_dict)

# mx_count = list(count_dict.values()).index(max(count_dict.values()))
# # print(count_dict, mx_count, count_dict.items())
# print(list(count_dict.keys())[mx_count])
# mx_count = 0
# mx_key = ''

# for k, v in count_dict.items():
#     if mx_count < v:
#         mx_key = k
#         mx_count = v
# print(mx_key)


# Условие
# Вам дан словарь, состоящий из пар слов. 
# Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.

# Для слова из словаря, записанного в последней строке, определите его синоним.

# Пример:
# 3
# Hello Hi
# Bye Goodbye
# List Array

# List -> Array
# Array -> List

count = int(input())
# words = dict() # {}

# for i in range(count):
#     try:
#         a, b = input().lower().split(' ')
#         words[a] = b
#         words[b] = a
#     except:
#         print('неверный формат данных')
#         break
words = {} # на подумать

# print(words[input('что мы ищем? ').lower()])
print(words.get(input('что ищем? '), 'такого слова нет в словаре'))


# Для каждого файла известно, с какими действиями можно к нему обращаться:

# запись W,
# чтение R,
# запуск X.
# В первой строке содержится число N — количество файлов содержащихся в данной файловой системе. 
# В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами. 
# Далее указано чиcло M — количество запросов к файлам. В последних M строках указан запрос вида Операция Файл. 
# К одному и тому же файлу может быть применено любое колличество запросов.

# Вам требуется проверить права доступа к файлам: 
# ваша программа для каждого запроса должна будет возвращать OK если над файлом выполняется допустимая операция, 
# или же Access denied, если операция недопустима.

# Пример:
# ввод:
# 4
# helloworld.exe R X
# pinglog W R
# nya R
# goodluck X W R
# 5
# read nya
# write helloworld.exe
# execute nya
# read pinglog
# write pinglog

# вывод:
# OK
# Access denied
# Access denied
# OK
# OK

# функции
def func_name(args):
    return True

def pow(x, y=2):
    return x ** y

def find_mx_mn(numbers):
    return max(numbers), min(numbers) # вернет кортеж
    # return [max(numbers), min(numbers)]

# const sq = (x) => {x ** 2}
sq = lambda x: x ** 2

# напишите функцию, нормализующую строку: удаляем двойные пробелы, приводит к нижнему рег
def norm(string):
    return string.lower().replace('  ', ' ')

norm_2 = lambda s: s.lower().replace('  ', ' ')
x = 3
print((lambda x: x ** 2)(x))

# ...rest spread...

x, y = [1, 2]
dict_6 = {'k1': 'v1', 'k2':'v2'}
key1, key2 = dict_6
dict_6[key1]

x, _, y = [1, 2, 3]

# упаковка
def pack(x, *tail):
    pass

pack(1, 2, 3, 4, 5) # -> x = 1, tail = [2, 3, 4, 5]

def pack(*head, x):
    pass

pack(1, 2, 3, 4, 5) # -> head = [1, 2, 3, 4], x = 5

def pack(x, *other, y):
    pass

pack(1, 2, 3, 4, 5) # -> x = 1, other = [2, 3, 4], y = 5

# распаковка
nums_1 = [1, 2, 3]
nums_2 = (4, 5, 6)

nums_3 = [*nums_1, *nums_2] 
# *[1, 2, 3] -> 1, 2, 3

# * - для массивов (списков), кортежей
# ** - для объектов (словарей)

def pack_dict(**dictionary):
    return dictionary

pack_dict(key="value", key2="value2") # -> {key: value, key2: value2}

dict_7 = {k1: v1}
dict_8 = {k2: v2}
dict_9 = {**dict_7, **dict_8} # -> {k1: v1, k2: v2}

# функции высшего порядка  (lazy iterators)
# map(func, iterables) iterables может быть несколько

def diff(x, y):
    return x - y

# [2, 2, 2] -> set() -> {2}
# ФВП возвращают специальные объекты
# map отталкивается от min(len(iterables))
map_1 = list(map(diff, {1, 2, 3}, [1, 2]))
print(map_1) # -> [0, 0], 3 из множества игнорируется

str_to_int = ['1', '2', '3']
k = 4
map_2 = list(map(lambda v, k=3: int(v) + k, str_to_int))
map_3 = list(map(int, str_to_int))

# ФВП не мутируют, а создают новый

# filter(func, iterable)
to_filter = [1, 2, 3, 4, 5, 6, 7]
only_odd = list(filter(lambda x: x % 2 != 0, to_filter))

obj = {
    'user1': 18,
    'user2': 46,
    'user3': 98
}

# для обработки объектов нужно преобразование в массив
# 1.
arr_obj = obj.items() # -> [('user1', 18), ....]
# 2.
filtered_age = list(filter(lambda user: user[1] > 30, arr_obj))
# 3. обратно в объект

# reduce нужно импортировать
# 1.
import functools
functools.reduce()
dir(functools) # справочник библиотеки

# 2.
from functools import reduce
reduce()

# 3.
import functools as f
f.reduce()

# 4.
from functools import *
reduce()


import math as m
import special_math as sm

m.sum()
sm.sum()

# map: на вход массив - на выход массив
# filter: на вход массив - на выход массив
# reduce: на вход массив - на выход что-то одно (аккумуляция)
to_reduce = [1, 2, 3]

def r_sum(acc, item):
    pass

sum_of_arr = reduce(lambda acc, item: acc + item, to_reduce) # ->
# 1. 0 + 1 -> acc = 1
# 2. 1 + 2 -> acc = 3
# 3. 3 + 3 -> acc = 6
# [1, 2, 3] -> 6

# напишите ф-цию, которая вычисляет факториал через reduce
# 3! = 1 * 2 * 3
# 5! = 1 * 2 * 3 * 4 * 5

# найти n!
def fact(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1), 1)
    
def fact_2(n):
    return 1 if n == 0 else reduce(lambda x, y: x * y, range(1, n + 1), 1)

# x > y ? True : False
# True if x > y else False