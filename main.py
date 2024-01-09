import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import platform
def get_os_info():
        return platform.uname()