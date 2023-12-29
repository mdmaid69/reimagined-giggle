import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import sys
def exit_program():
        sys.exit()