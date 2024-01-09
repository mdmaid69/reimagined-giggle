import collections
def create_user_list():
        return collections.UserList()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)