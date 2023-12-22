import platform
def get_os_info():
        return platform.uname()
import array
def extend_array(array, iterable):
        array.extend(iterable)