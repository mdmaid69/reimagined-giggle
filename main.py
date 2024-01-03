import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)