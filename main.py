import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)