import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import platform
def get_os_info():
        return platform.uname()