import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def find_union(list1, list2):
        return set(list1) | set(list2)