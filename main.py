import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))