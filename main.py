import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def add_numbers(a, b):
        return a + b