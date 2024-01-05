import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a