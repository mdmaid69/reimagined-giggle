import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)