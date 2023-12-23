import math
def calculate_sign(x):
        return math.copysign(1, x)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()