import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))