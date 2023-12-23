import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)