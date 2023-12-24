sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])