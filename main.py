import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import shutil
def delete_directory(path):
        shutil.rmtree(path)