import array
def convert_array_to_list(array):
        return array.tolist()
def find_common_elements(list1, list2):
        return set(list1) & set(list2)