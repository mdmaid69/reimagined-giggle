import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)