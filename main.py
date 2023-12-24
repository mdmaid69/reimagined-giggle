import array
def get_array_as_bytearray(array):
        return bytearray(array)
import platform
def get_os_info():
        return platform.uname()