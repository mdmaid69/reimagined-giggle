import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()