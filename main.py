import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()