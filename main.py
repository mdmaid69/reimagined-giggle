import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)