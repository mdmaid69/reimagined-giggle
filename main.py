import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import math
def calculate_circle_area(radius):
        return math.pi * radius**2