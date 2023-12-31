import sys
def print_python_version():
        print(sys.version)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)