import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def cube_number(x):
        return x**3