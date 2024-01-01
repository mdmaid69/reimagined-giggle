sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)