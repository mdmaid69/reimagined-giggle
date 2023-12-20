import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def find_union(list1, list2):
        return set(list1) | set(list2)