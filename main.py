import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import platform
def get_os_info():
        return platform.uname()