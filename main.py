import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)