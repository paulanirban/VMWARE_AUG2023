
"""
what are lambdas
----------------
anonymous function with a single expression

lambda arg1, arg2, arg3.....: expression

"""

def add(x, y):
    return x + y

a = add
print(a(10, 20))
print("-" * 60)

b = lambda a, b: a + b
print(b(100, 200))

# lambdas - map, filter and reduce

print("-" * 60)
# map - that will implement the expression on all data that is passed
# filter - that will implement the expression on all data in such a way that== it either returns a true or a false
# reduce - that will implement a formula and the returns a single val as a result

l1 = list(range(1, 11))
print(f"l1 :{l1}")
squares = list(map(lambda x : x ** 2, l1))
print(f"squares :{squares}")

print("-" * 60)
months = ['dec', 'aug', 'oct', 'jul', 'jan', 'nov', 'apr', 'sep', 'feb', 'may', 'jun', 'mar']
print(f"unsorted months :{months}")
from calendar import month_abbr, month_name
print(list(month_abbr))
# print(list(month_name))
res = sorted(months, key = list(map(lambda x: x.lower(), list(month_abbr))).index)
print(f"Sorted Months :{res}")

print("Filter".center(60,"-"))
l1 = list(range(1, 25))
print(f"l1 :{l1}")
res = list(filter(lambda x: x % 3 == 0, l1))
print(f"res :{res}")

st = "the quick brown fox jumps over the lazy dog"
words = st.split()
print(words)
res = list(filter(lambda x : x != "the", words))
print(f"res :{res}")

print("reduce".center(60,"-"))
from functools import reduce
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")

l1 = [3, 7, 10, 1, 8, 2, 9, 5, 6, 4]
print(f"l1 :{l1}")
res = reduce(lambda x, y: x if x > y else y, l1)
print(f"res :{res}")

print("-" * 60)

