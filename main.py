import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import shutil
def delete_directory(path):
        shutil.rmtree(path)