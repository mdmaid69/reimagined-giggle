import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import shutil
def delete_directory(path):
        shutil.rmtree(path)