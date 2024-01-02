def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()