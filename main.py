import platform
def get_os_info():
        return platform.uname()
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)