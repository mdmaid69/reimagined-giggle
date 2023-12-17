import os
def list_files_in_directory(path):
        return os.listdir(path)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)