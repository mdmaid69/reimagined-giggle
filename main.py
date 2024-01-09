import array
def get_array_length(array):
        return len(array)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)