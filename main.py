def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)