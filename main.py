list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)