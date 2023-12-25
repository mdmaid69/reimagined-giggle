import getpass
def get_username():
        return getpass.getuser()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)