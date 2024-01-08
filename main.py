import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)