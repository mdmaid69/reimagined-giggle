import collections
def create_user_list():
        return collections.UserList()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)