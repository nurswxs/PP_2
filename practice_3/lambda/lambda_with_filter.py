#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#2
numbers = [1, 3, 5, 7, 2, 4, 6]
greater_than_4 = list(filter(lambda x: x > 4, numbers))
print(greater_than_4)  # [5, 7, 6]

#3
words = ["cat", "dog", "elephant", "lion"]
long_words = list(filter(lambda x: len(x) > 3, words))
print(long_words)  # ['elephant', 'lion']


#4
words = ["apple", "banana", "cherry", "dog"]
a_words = list(filter(lambda x: 'a' in x, words))
print(a_words)  # ['apple', 'banana']