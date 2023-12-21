import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def is_odd(n):
        return n % 2 != 0