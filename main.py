import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import sys
def add_to_python_path(path):
        sys.path.append(path)