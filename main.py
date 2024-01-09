import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)