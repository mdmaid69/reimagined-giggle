import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import collections
def create_user_list():
        return collections.UserList()