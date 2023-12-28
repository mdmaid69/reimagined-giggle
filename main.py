import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def calculate_area(radius):
        return 3.14 * radius * radius