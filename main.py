import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))