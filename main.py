text = "Hello, world!"
print("Characters:", len(text))
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)