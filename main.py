import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import collections
def create_user_dict():
        return collections.UserDict()