import math
def calculate_sign(x):
        return math.copysign(1, x)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)