import getpass
def get_username():
        return getpass.getuser()
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a