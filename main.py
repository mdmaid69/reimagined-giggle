import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def sort_numbers(numbers):
        return sorted(numbers)