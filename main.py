print([x**2 for x in range(10)])
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()