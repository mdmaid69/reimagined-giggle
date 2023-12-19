import collections
def create_user_dict():
        return collections.UserDict()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)