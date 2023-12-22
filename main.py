import math
def calculate_exponential(x):
        return math.exp(x)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()