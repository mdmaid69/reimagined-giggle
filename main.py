import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)