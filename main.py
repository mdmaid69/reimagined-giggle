import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)