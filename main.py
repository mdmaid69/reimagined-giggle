import platform
def get_os_info():
        return platform.uname()
import array
def get_array_as_int(array):
        return int(array[0])