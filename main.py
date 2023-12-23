import math
def calculate_circle_area(radius):
        return math.pi * radius**2
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()