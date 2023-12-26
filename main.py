import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import collections
def create_user_dict():
        return collections.UserDict()