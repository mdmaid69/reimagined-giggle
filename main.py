import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)