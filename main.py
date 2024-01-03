import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)