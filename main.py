import math
def calculate_cosine(x):
        return math.cos(x)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()