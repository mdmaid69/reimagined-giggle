import array
def get_array_as_memoryview(array):
        return memoryview(array)
import getpass
def get_username():
        return getpass.getuser()