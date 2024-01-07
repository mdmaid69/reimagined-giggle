import platform
def get_os_info():
        return platform.uname()
import array
def get_array_typecode(array):
        return array.typecode