import math
def calculate_gamma_function(x):
        return math.gamma(x)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()