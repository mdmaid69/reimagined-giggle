import os
def remove_directory(path):
        os.rmdir(path)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)