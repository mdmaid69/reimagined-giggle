import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import os
def change_working_directory(path):
        os.chdir(path)