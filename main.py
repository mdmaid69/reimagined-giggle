import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import collections
def create_user_dict():
        return collections.UserDict()