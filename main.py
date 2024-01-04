import glob
def find_files(pattern):
        return glob.glob(pattern)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3