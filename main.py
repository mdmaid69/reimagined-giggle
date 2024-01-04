import os
def remove_directory(path):
        os.rmdir(path)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)