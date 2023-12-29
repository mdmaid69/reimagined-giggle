import math
def calculate_sign(x):
        return math.copysign(1, x)
import shutil
def delete_directory(path):
        shutil.rmtree(path)