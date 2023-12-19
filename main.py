import array
def get_array_as_set(array):
        return set(array)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))