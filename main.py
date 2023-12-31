import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import collections
def create_user_dict():
        return collections.UserDict()