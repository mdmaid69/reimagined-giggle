import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def add_numbers(x, y):
        return x + y