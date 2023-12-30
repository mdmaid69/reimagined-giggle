import shutil
def delete_directory(path):
        shutil.rmtree(path)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)