import array
def get_array_as_memoryview(array):
        return memoryview(array)
def find_difference(list1, list2):
        return set(list1) - set(list2)