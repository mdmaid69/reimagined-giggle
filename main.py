import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))