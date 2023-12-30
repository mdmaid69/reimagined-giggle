import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)