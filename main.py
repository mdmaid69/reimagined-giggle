import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()