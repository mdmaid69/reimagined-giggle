import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()