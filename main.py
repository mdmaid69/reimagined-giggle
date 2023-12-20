import array
def extend_array(array, iterable):
        array.extend(iterable)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))