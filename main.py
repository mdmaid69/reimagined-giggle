import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def find_min(numbers):
        return min(numbers)