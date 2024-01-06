import collections
def create_user_dict():
        return collections.UserDict()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)