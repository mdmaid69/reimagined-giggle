import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)