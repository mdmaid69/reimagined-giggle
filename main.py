import array
def get_array_buffer_info(array):
        return array.buffer_info()
def find_common_elements(list1, list2):
        return set(list1) & set(list2)