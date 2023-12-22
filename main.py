import platform
def get_os_info():
        return platform.uname()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)