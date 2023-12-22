import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import shutil
def delete_directory(path):
        shutil.rmtree(path)