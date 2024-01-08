import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)