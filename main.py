import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import array
def convert_array_to_string(array):
        return array.tostring()