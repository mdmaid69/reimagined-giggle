sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])