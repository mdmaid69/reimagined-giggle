import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()