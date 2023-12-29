import collections
def create_ordered_dict():
        return collections.OrderedDict()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)