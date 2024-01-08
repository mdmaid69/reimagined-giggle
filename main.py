import getpass
def get_username():
        return getpass.getuser()
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a