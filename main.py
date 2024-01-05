def find_union(list1, list2):
        return set(list1) | set(list2)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)