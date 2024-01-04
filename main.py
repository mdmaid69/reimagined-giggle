import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)