import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def calculate_volume(length, width, height):
        return length * width * height