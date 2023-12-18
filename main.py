import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)