import os
def get_environment_variable(var):
        return os.getenv(var)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a