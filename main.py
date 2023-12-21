import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)