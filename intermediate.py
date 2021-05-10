"""Lists
"""

"""Tuples
"""

"""Dictionaries
"""

"""Sets
"""

"""Strings
"""

"""Collections
"""
# from collections import Counter, namedtuple, defaultdict, deque

# a = "aaaaabbbbccc"
# my_counter = Counter(a)
# print(my_counter)
# print(list(my_counter.elements()))

# Point = namedtuple('Point', 'x, y')
# pt = Point(1, 4)
# print(pt)
# print(pt.x, pt.y)

# d = defaultdict(int)
# print(d['new_item'])

# d = deque()
# d.append(1)
# d.append(2)
# d.appendleft(3)
# print(d)
# d.extendleft([4,5,6])
# print(d)
# d.rotate(1)
# print(d)

"""Itertools
"""
# from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat

# a = [1, 2]
# b = [3, 4]
# print(list(product(a, b)))

# a = [1, 2, 3]
# print(list(permutations(a, 3)))

# a = [1, 2, 3, 4]
# print(list(combinations(a, 3)))

# a = [1, 2, 3, 4]
# print(list(combinations_with_replacement(a, 3)))

# import operator
# a = [1, 2, 3, 4]
# print(list(accumulate(a)))
# print(list(accumulate(a, func=operator.mul)))

# a = [1,2,3,4]
# group_by = groupby(a, key=lambda x: x < 3)
# for key, val in group_by:
#     print(key, list(val))

# persons = [
#     {'name': 'Tim', 'age': 25},
#     {'name': 'John', 'age': 29},
#     {'name': 'Tom', 'age': 35},
# ]
# group_by = groupby(persons, key=lambda x: x['age'])
# for key, val in group_by:
#     print(key, list(val))

# for i in count(10):
#     print(i)
#     if i == 15:
#         break

# a = [1, 2, 3]
# n = 0
# for i in cycle(a):
#     print(i)
#     n += 1
#     if n == 5:
#         break

# n = 0
# for i in repeat(1):
#     print(i)
#     n += 1
#     if n == 5:
#         break


"""Lambda
"""
# from functools import reduce

# points2D = [(1,2), (15,1), (3,6)]
# sorted_points2D = sorted(points2D, key=lambda x: x[1])
# print(sorted_points2D)

# a = [1,2,3,4]
# b = map(lambda x: x*2, a)
# c = filter(lambda x: x%2==0, a)
# d = reduce(lambda x,y: x*y , a)
# print(list(b))
# print(list(c))
# print(d)

"""Exception
"""

# # raise
# x = -5
# if x < 0:
#     raise Exception("x should greater then 0")

# # assert
# x = -5
# assert(x >=0 ), "x should greater then 0"

# # try-exception
# 1.
# try:
#     x = 5 / 0
# except Exception as e:
#     print(e)

# 2.
# try:
#     a = 5 / 0
#     b = a + 10
# except ZeroDivisionError as e:
#     print("Err:")
#     print(e)
# except TypeError as e:
#     print("Err")
#     print(e)
# else:
#     print("ok")
#     print(b)
# finally:
#     print("exit...")

# 3.
# class ValueTooHighErr(Exception):
#     pass

# class ValueTooSmallErr(Exception):
#     def __init__(self, message, value):
#         self.message = message
#         self.value = value

# def test_value(x):
#     if x > 100:
#         raise ValueTooHighErr('value too high')
#     if x < 5:
#         raise ValueTooSmallErr('value too small', x)

# test_value(0)

"""Logging
"""
import logging

# logging format
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S',
    level=logging.DEBUG
)

# 5 logging levels
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")



