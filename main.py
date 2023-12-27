text = "Hello, world!"
print("Uppercase:", text.upper())
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)