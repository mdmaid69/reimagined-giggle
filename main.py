import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()