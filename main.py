import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)