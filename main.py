import platform
def get_python_version():
        return platform.python_version()
import array
def get_array_buffer_info(array):
        return array.buffer_info()