import getpass
def get_username():
        return getpass.getuser()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)