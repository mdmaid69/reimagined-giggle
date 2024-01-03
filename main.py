import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)