import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import collections
def create_user_string():
        return collections.UserString()