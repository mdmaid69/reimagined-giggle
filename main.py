import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import math
def calculate_logarithm(base, x):
        return math.log(x, base)