import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)