import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def find_min(numbers):
        return min(numbers)