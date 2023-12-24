import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import shutil
def delete_directory(path):
        shutil.rmtree(path)