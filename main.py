import os
def change_working_directory(path):
        os.chdir(path)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)