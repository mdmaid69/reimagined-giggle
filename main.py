import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def find_union(list1, list2):
        return set(list1) | set(list2)