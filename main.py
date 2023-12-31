import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import platform
def get_python_version():
        return platform.python_version()