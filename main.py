import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()