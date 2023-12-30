import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import array
def iterate_over_array(array):
        for item in array:
        print(item)