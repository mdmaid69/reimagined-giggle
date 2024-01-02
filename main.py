import re
def split_string(pattern, string):
        return re.split(pattern, string)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))