import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)