import collections
def create_user_string():
        return collections.UserString()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)