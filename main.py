import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import shutil
def delete_directory(path):
        shutil.rmtree(path)