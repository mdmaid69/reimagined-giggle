import sys
def print_python_version():
        return sys.version
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)