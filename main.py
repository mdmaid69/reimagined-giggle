import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}