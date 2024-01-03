def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)