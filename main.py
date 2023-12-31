import array
def get_list_from_array(array):
        return array.tolist()
def find_common_elements(list1, list2):
        return set(list1) & set(list2)