import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)