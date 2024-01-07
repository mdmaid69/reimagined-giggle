import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def calculate_area(radius):
        return 3.14 * radius * radius