import collections
def create_user_string():
        return collections.UserString()
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)