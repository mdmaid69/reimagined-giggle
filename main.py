import glob
def find_files(pattern):
        return glob.glob(pattern)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height