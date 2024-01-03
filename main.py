import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))