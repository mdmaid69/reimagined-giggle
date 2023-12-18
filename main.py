import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()