import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()