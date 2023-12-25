import array
def get_list_from_array(array):
        return array.tolist()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)