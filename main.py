import getpass
def get_username():
        return getpass.getuser()
import glob
def find_files(pattern):
        return glob.glob(pattern)