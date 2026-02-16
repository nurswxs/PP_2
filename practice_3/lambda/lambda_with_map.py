#1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#2
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

#3
fruits = ["apple", "banana", "cherry"]
upper_fruits = list(map(lambda x: x.upper(), fruits))
print(upper_fruits)  # ['APPLE', 'BANANA', 'CHERRY']

#4
words = ["cat", "elephant", "dog"]
lengths = list(map(lambda x: len(x), words))
print(lengths)  # [3, 8, 3]

#5
numbers = [1, -2, 3, -4, 5]
negated = list(map(lambda x: -x, numbers))
print(negated)  # [-1, 2, -3, 4, -5]