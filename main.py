def remove_duplicates(lst):
        return list(set(lst))
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)