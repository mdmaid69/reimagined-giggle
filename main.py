import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)