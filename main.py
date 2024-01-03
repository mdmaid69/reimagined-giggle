import collections
def create_user_list():
        return collections.UserList()
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a