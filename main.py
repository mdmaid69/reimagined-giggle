import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)