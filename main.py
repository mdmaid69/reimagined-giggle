import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def find_max(numbers):
        return max(numbers)