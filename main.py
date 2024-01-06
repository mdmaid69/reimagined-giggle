import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)