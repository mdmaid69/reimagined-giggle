import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)