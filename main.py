import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()