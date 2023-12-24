import getpass
def get_username():
        return getpass.getuser()
import array
def get_array_as_memoryview(array):
        return memoryview(array)