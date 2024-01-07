import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def square_number(x):
        return x**2