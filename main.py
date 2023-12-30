import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
def calculate_perimeter_triangle(a, b, c):
        return a + b + c