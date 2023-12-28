import array
def get_array_as_frozenset(array):
        return frozenset(array)
def find_difference(list1, list2):
        return set(list1) - set(list2)