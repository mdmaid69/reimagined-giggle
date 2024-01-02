import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)