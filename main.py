import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable