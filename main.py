import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))