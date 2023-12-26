import array
def remove_from_array(array, item):
        array.remove(item)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))