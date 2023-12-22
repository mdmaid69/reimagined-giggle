import sys
def add_to_python_path(path):
        sys.path.append(path)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)