import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import shutil
def delete_directory(path):
        shutil.rmtree(path)