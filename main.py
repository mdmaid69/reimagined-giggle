list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable