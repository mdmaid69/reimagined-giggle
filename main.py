import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))