import getpass
def get_username():
        return getpass.getuser()
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable