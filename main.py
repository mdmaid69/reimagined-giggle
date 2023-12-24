import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def calculate_perimeter_triangle(a, b, c):
        return a + b + c