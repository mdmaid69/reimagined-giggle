import glob
def find_files(pattern):
        return glob.glob(pattern)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)