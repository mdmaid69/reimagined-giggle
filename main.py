import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)