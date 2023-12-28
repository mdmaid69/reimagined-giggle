import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))