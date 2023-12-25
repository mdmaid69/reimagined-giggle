import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()