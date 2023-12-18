import array
def insert_into_array(array, i, item):
        array.insert(i, item)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))