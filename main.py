import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)