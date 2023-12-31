import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()