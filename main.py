n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()