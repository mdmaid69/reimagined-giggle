import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)