import array
def get_array_as_bytearray(array):
        return bytearray(array)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)