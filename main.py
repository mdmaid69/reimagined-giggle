import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()