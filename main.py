import collections
def create_user_string():
        return collections.UserString()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)