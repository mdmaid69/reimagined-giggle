import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)