import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)