def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))