import sys
def add_to_python_path(path):
        sys.path.append(path)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)