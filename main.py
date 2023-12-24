import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)