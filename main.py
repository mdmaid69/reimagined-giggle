def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)