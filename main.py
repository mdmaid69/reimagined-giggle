import collections
def create_user_dict():
        return collections.UserDict()
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a