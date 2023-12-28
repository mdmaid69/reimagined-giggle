import platform
def get_os_info():
        return platform.uname()
import array
def get_array_buffer_info(array):
        return array.buffer_info()