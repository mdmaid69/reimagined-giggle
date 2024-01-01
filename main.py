n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()