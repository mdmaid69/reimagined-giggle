n = 10
print("Square numbers:", [x**2 for x in range(n)])
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()