import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))