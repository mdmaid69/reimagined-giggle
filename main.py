import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))