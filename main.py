import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)