import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import sys
def print_python_version():
        print(sys.version)