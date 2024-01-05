import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()