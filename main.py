import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()