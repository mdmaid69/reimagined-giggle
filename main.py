import re
def split_string(pattern, string):
        return re.split(pattern, string)
def find_difference(list1, list2):
        return set(list1) - set(list2)