list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
def find_common_elements(list1, list2):
        return set(list1) & set(list2)