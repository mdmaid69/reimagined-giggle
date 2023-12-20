def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}