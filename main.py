import array
def get_array_slice(array, i, j):
        return array[i:j]
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))