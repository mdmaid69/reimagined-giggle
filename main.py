def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()