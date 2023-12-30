import collections
def create_user_list():
        return collections.UserList()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}