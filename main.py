import platform
def get_os_info():
        return platform.uname()
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)