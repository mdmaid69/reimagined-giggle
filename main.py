import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)