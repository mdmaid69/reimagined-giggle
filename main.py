import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))