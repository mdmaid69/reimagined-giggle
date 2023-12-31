import getpass
def get_username():
        return getpass.getuser()
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)