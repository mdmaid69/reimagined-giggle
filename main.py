import platform
def get_os_info():
        return platform.uname()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)