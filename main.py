import re
print(re.match("h.*o", "hello world"))
def find_common_elements(list1, list2):
        return set(list1) & set(list2)