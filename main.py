import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)