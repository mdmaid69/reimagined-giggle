import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()