import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)