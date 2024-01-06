import platform
def get_os_info():
        return platform.uname()
import collections
def count_elements(iterable):
        return collections.Counter(iterable)