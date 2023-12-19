import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)