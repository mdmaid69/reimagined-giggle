import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)