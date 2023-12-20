import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def multiply_numbers(x, y):
        return x * y