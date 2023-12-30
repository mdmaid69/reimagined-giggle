import sys
def print_python_version():
        print(sys.version)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)