import os
def get_file_size(filename):
        return os.path.getsize(filename)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3