import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a