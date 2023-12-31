import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()