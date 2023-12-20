print("Hello, world!")
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)