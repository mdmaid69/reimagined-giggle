import collections
def create_user_dict():
        return collections.UserDict()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)