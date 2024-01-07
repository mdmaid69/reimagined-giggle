import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import os
def list_files_in_directory(path):
        return os.listdir(path)