import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import math
def calculate_tangent(x):
        return math.tan(x)