import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import getpass
def get_username():
        return getpass.getuser()