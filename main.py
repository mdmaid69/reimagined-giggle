def calculate_volume(length, width, height):
        return length * width * height
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)