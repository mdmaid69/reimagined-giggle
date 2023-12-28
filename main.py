import getpass
def get_username():
        return getpass.getuser()
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()