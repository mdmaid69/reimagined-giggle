import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)