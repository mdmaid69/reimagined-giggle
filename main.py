import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def remove_duplicates(lst):
        return list(set(lst))