import array
def get_bytes_from_array(array):
        return array.tobytes()
def find_common_elements(list1, list2):
        return set(list1) & set(list2)