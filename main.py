def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)