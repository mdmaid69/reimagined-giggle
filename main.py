import os
def get_file_size(filename):
        return os.path.getsize(filename)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)