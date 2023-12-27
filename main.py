import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def is_even(n):
        return n % 2 == 0