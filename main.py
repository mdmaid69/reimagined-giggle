import platform
def get_os_info():
        return platform.uname()
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array