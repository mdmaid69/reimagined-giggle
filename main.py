import platform
def get_python_version():
        return platform.python_version()
import collections
def count_elements(iterable):
        return collections.Counter(iterable)