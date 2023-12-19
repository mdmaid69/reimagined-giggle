import array
def get_array_as_int(array):
        return int(array[0])
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)