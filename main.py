import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)