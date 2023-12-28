import shutil
def delete_directory(path):
        shutil.rmtree(path)
import getpass
def get_username():
        return getpass.getuser()