import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()