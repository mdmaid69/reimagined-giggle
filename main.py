import sys
def add_to_python_path(path):
        sys.path.append(path)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)