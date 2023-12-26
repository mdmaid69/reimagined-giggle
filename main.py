import platform
def get_os_info():
        return platform.uname()
import array
def check_if_array_contains_item(array, item):
        return item in array