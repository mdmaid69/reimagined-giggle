import math
def calculate_error_function(x):
        return math.erf(x)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()