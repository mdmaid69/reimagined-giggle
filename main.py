import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)