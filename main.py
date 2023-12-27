import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import shutil
def delete_directory(path):
        shutil.rmtree(path)