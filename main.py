text = "Hello, world!"
print("Reversed:", text[::-1])
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()