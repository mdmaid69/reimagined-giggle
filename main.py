import platform
def get_python_version():
        return platform.python_version()
def find_common_elements(list1, list2):
        return set(list1) & set(list2)