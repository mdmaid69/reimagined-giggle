import getpass
def get_username():
        return getpass.getuser()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)