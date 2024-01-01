import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()