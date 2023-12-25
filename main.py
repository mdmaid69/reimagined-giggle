import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)