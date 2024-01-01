import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)