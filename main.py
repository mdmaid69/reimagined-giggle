import os
def get_current_working_directory():
        return os.getcwd()
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)