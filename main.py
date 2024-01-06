import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()