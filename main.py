import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)