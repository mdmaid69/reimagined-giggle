import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)