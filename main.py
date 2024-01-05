import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import sys
def add_to_python_path(path):
        sys.path.append(path)