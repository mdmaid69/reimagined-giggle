import shutil
def delete_directory(path):
        shutil.rmtree(path)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)