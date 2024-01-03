import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)