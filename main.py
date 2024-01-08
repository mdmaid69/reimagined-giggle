import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()