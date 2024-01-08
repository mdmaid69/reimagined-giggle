import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)