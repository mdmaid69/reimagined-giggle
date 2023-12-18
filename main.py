import os
def get_environment_variable(var):
        return os.getenv(var)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)