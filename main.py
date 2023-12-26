import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)