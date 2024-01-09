import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import getpass
def get_username():
        return getpass.getuser()