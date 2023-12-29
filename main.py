import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height