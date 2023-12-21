import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import math
def calculate_sign(x):
        return math.copysign(1, x)