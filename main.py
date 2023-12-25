import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import collections
def create_user_list():
        return collections.UserList()