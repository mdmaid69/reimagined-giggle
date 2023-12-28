sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])