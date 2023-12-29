import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3