import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))