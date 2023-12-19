list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)