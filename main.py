import getpass
def get_username():
        return getpass.getuser()
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)