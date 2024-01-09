list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)