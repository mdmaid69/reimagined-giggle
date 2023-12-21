import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import os
def get_file_size(filename):
        return os.path.getsize(filename)