def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()