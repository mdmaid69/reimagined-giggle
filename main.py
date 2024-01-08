import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)