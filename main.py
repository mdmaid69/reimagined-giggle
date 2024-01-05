import os
def get_environment_variable(var):
        return os.getenv(var)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)