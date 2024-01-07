import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()