import platform
def get_python_version():
        return platform.python_version()
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array