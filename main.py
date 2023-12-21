import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)