import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import platform
def get_python_version():
        return platform.python_version()