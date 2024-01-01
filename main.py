import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height