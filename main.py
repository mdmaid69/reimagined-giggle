import platform
def get_python_version():
        return platform.python_version()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)