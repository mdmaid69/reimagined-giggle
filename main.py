import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()