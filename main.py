import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)