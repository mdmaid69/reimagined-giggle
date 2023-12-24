import os
def get_file_size(filename):
        return os.path.getsize(filename)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)