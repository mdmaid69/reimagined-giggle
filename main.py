import platform
def get_os_info():
        return platform.uname()
import array
def get_array_itemsize(array):
        return array.itemsize