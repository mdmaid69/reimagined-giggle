import collections
def create_user_dict():
        return collections.UserDict()
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a