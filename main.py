import platform
def get_os_info():
        return platform.uname()
import array
def remove_from_array(array, item):
        array.remove(item)