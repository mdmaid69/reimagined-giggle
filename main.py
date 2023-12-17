import getpass
def get_username():
        return getpass.getuser()
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)