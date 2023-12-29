import re
def split_string(pattern, string):
        return re.split(pattern, string)
import collections
def create_user_dict():
        return collections.UserDict()