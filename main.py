import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)