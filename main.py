import array
def get_list_from_array(array):
        return array.tolist()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))