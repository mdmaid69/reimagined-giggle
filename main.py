import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()