import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)