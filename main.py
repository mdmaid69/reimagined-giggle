import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)