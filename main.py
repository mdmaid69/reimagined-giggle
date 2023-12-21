import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import sys
def print_python_version():
        print(sys.version)