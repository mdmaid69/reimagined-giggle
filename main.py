import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import collections
def create_user_list():
        return collections.UserList()