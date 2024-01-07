def find_union(list1, list2):
        return set(list1) | set(list2)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))