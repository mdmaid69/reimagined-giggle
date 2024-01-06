import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)