import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))