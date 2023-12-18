import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)