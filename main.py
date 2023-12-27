import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()