import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3