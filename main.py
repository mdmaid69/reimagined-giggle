sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))