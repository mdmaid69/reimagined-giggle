import glob
def find_files(pattern):
        return glob.glob(pattern)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)