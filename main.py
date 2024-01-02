import os
def list_files_in_directory(path):
        return os.listdir(path)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)