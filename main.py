import collections
def create_user_list():
        return collections.UserList()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)