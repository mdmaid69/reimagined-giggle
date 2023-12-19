import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
def find_common_elements(list1, list2):
        return set(list1) & set(list2)