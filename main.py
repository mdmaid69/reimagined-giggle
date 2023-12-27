import array
def convert_array_to_list(array):
        return array.tolist()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))