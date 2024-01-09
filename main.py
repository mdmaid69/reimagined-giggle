sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)