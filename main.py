import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height