import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()