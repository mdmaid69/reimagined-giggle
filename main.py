import shutil
def delete_directory(path):
        shutil.rmtree(path)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)