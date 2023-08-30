l = list(range(1, 11))
squares = [lst ** 2 for lst in l]
print(f"squares :{squares}")

print("-" * 60)

fruits = [
    ('apple', 280),
    ('orange', 160),
    ('pineapple', 85),
    ('grapes', 130),
    ('watermelon', 70),
    ('banana', 65),
    ('gauva', 110),
    ('strawberry', 350)
]

print(f"fruits : {fruits}")

print("-" * 60)
prices = ["fruit" for fruit in fruits]
print(f"prices :{prices}")

print("-" * 60)
prices = [fruit for fruit in fruits]
print(f"prices :{prices}")

print("-" * 60)
prices = [fruit[0] for fruit in fruits]
print(f"prices :{prices}")

print("-" * 60)
prices = [fruit[1] for fruit in fruits]
print(f'prices :{prices}')

print("-" * 60)
prices = [fruit[1] * 0.9 for fruit in fruits]
print(f"prices :{prices}")

print("-" * 60)
prices = [fruit[1] * 0.75 for fruit in fruits]
print(f"prices :{prices}")

print("-" * 60)
prices = [fruit[1] * 0.75 for fruit in fruits if fruit[0] != 'apple']
print(f"prices :{prices}")

print("-" * 60)
prices = [[fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75]
          for fruit in fruits if fruit[1] > 100]
print(f"prices :{prices}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

words = [word for word in sentence.split()]
print(f"words :{words}")

print("-" * 60)
words = [word for word in sentence.split() if word != 'the']
print(f"words :{words}")

print("-" * 60)
words = [word for word in sentence.split() if len(word) > 3]
print(f"words :{words}")

print("-" * 60)
def square(x):
    return x ** 2

l1 = list(range(1, 11))
sqr = list(map(square, l1))
print(sqr)

print("-" * 60)

sqr = list(map(lambda x: square(x), l1))
print(sqr)
