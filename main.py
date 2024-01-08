import array
def get_array_as_frozenset(array):
        return frozenset(array)
import platform
def get_os_info():
        return platform.uname()