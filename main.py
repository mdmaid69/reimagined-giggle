import array
def convert_array_to_list(array):
        return array.tolist()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)