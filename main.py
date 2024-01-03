sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])